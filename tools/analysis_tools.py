import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime
import copy
from scipy.optimize import curve_fit
from sdRDM import DataModel
from tabulate import tabulate
from scipy.integrate import trapz
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual
import re
from IPython.display import display
lib = DataModel.from_markdown("specifications/Electrochemistry.md")
# path_program=os.getcwd()
# print(path_program)

class ReferenceCalculator:
    def __init__(self,e_chem,experiment_list=None):
        """Dictionary with the reference names and potentials """
        self.reference_values = {
            "SHE": 0, 
            "RHE": -0.0591, 
            "Hg/Hg2Cl2 (0.1 M KCl)": 0.334,
            "Hg/Hg2Cl2 (1 M KCl)": 0.280,
            "Hg/Hg2Cl2 (3.5 M KCl)": 0.250,
            "Hg/Hg2Cl2 (sat. KCl)": 0.241,
            "Hg/Hg2SO4 (0.5 M H2SO4)": 0.682,
            "Hg/Hg2SO4 (1 M H2SO4)": 0.674, 
            "Hg/Hg2SO4 (sat. K2SO4)": 0.65,
            "Ag/AgCl (0.1 M KCl)": 0.2881, 
            "Ag/AgCl (3 M KCl)": 0.21,
            "Ag/AgCl (3.5 M KCl)": 0.205,
            "Ag/AgCl (sat. KCl)": 0.199,
            "Ag/Ag2SO4 (0.5 M H2SO4)": 0.72,
            "Ag/Ag2SO4 (1 M H2SO4)": 0.71,
            "Ag/Ag2SO4 (sat. K2SO4)": 0.68,
            "Hg/HgO (0.1 M NaOH)": 0.165,
            "Hg/HgO (1 M NaOH)": 0.140,
            "Fc/Fc+ (0.05 M  nBu4NPF6/MeCN)":0.64,
        }
        self.e_chem=e_chem
        self.experiment_list=experiment_list
        self.table = [[old_reference, new_reference] for old_reference, new_reference in self.reference_values.items()]

    def reference_list(self):
        """ A method, which returns a table"""
        print(tabulate(self.table, headers=["Reference", "Potential vs. (NHE) (V)"]))

    def reference_difference(self):
        """Extract method to save only the reference name without the concentration"""
        def extract_name(reference):
            return reference.split('(')[0].strip()
        def interactive(old_reference="Ag/AgCl (sat. KCl)", new_reference="SHE", pH="1", potential="0"):
            if old_reference == "RHE" or new_reference == "RHE":
                self.reference_values["RHE"] = -0.0592 * float(pH)
            self.reference_difference_value = float(potential) + self.reference_values[new_reference] - self.reference_values[old_reference]
            new_reference_name = extract_name(new_reference)
            """Interactive button to save the potential values into the data model"""
            def on_button_click(_):
                    for experiment in self.experiment_list:
                        if self.e_chem.experiments[experiment].type == "CP" and (self.reference_difference_value, new_reference_name) not in self.e_chem.experiments[experiment].analysis.cp.change_potential:
                            self.e_chem.experiments[experiment].analysis.cp.change_potential.append((self.reference_difference_value, new_reference_name))
                            print("Potential value:", self.reference_difference_value, new_reference_name,"was saved to experiment:", experiment)
                        elif self.e_chem.experiments[experiment].type == "CV" and (self.reference_difference_value, new_reference_name) not in self.e_chem.experiments[experiment].analysis.cv.change_potential:
                            self.e_chem.experiments[experiment].analysis.cv.change_potential.append((self.reference_difference_value, new_reference_name))
                        elif self.e_chem.experiments[experiment].type == "CA":
                            print("Experiment is from type CA and don't need a change_potential value")
                        else:
                            print("Reference potential is already saved")
                            break    

            button = widgets.Button(description="Potential2Model")
            button.on_click(on_button_click)
            display(button)
            return self.reference_difference_value

        widgets.interact(interactive, old_reference=list(self.reference_values.keys()), new_reference=list(self.reference_values.keys()))
        
        


class Chronopotentiometry:
    def __init__(self,e_chem,experiment_list,change_reference_list_index=None,change_reference=False):
        self.e_chem = e_chem
        self.experiment_list=experiment_list
        self.df_liste=[]
        self.induced_current_density=self.e_chem.experiments[experiment_list[0]].analysis.cp.induced_current[0]/ self.e_chem.experiments[experiment_list[0]].electrode_setup.working_electrode_area
        """ Mapping dictionary for the area units"""
        mapping_dict={"cm^2":"cm$^2$",
                      "mm^2":"mm$^2$"}
        area_unit=mapping_dict[self.e_chem.experiments[experiment_list[0]].electrode_setup.working_electrode_area_unit]
        self.induced_current_density_unit=self.e_chem.experiments[experiment_list[0]].analysis.cp.induced_current_unit + "/"+ area_unit
        """Method that add the experiments into the self.df_liste"""
        for experiment in range(0,len(self.e_chem.experiments)):
            if self.e_chem.experiments[experiment].type=="CP":
                """ Reader to find the header line"""
                with open(self.e_chem.experiments[experiment].filename, 'r') as file:
                    for line_num, line in enumerate(file, start=1):
                        if re.match(r'CURVE\sTABLE\s3600', line):
                            header=line_num+2
                            break
                df = pd.read_csv(self.e_chem.experiments[experiment].filename, sep="\t", header=header, usecols=[2,3,4,5],names=["t","E","I","V"])
                self.df_liste.append(df)
            else:
                self.df_liste.append(None)
        """ Mapping dictionary for the correct reference scale names """
        self.mapping_dict_reference_names={"SHE":"SHE",
                      "RHE":"RHE",
                      "Hg/Hg2Cl2": "Hg/Hg$_2$Cl$_2$",
                      "Ag/AgCl":"Ag/AgCl",
                      "Ag/Ag2SO4": "Ag/Ag$_2$SO$_4$",
                      "Hg/HgO": "Hg/HgO",
                      "Hg/Hg2SO4":"Hg/Hg$_2$SO$_4$",
                      "Fc/Fc+": "Fc/Fc$^{+}"}
        self.reference = self.mapping_dict_reference_names[self.e_chem.experiments[experiment_list[0]].electrode_setup.reference_electrode]
        self.reference_name=self.e_chem.experiments[experiment_list[0]].electrode_setup.reference_electrode
        self.xlabel=f"$t$ ({self.e_chem.experiments[experiment_list[0]].analysis.cp.measurement_time_unit})"
        self.ylabel=f"$E$ vs. {self.reference} ({self.e_chem.experiments[experiment_list[0]].analysis.cp.measurement_potential_unit})"
        """ The change_reference statement, which allow the transformation and work with a new reference scale"""
        if change_reference:
            self.delta_E=self.e_chem.experiments[experiment_list[0]].analysis.cp.change_potential[change_reference_list_index][0]
            self.reference=self.mapping_dict_reference_names[self.e_chem.experiments[experiment_list[0]].analysis.cp.change_potential[change_reference_list_index][1]]
            self.reference_name=self.e_chem.experiments[experiment_list[0]].analysis.cp.change_potential[change_reference_list_index][1]
            self.ylabel=f"$E$ vs. {self.reference} ({self.e_chem.experiments[experiment_list[0]].analysis.cp.measurement_potential_unit})"
            for df in self.df_liste:
                if df is not None:
                    df['E'] = df['E'] + self.delta_E
        else:
             self.delta_E = 0


    def quick_plot(self):
        """ Quick plot method, which allows to see the potential, the current and the potential in the whole cell"""
        for experiment in self.experiment_list:
            f, (ax,ax2,ax3) = plt.subplots(3,1)
            f.suptitle(self.e_chem.experiments[experiment].name)
            ax.plot(self.df_liste[experiment]["t"], self.df_liste[experiment]["E"])
            ax2.plot(self.df_liste[experiment]["t"], self.df_liste[experiment]["I"])
            ax3.plot(self.df_liste[experiment]["t"], self.df_liste[experiment]["V"])
            ax.set_ylabel("$E$ vs Ref (V)")
            ax2.set_ylabel("$I$ (A)")
            ax3.set_ylabel("$V$ (V)")
            ax3.set_xlabel("$t$ (s)")
            ax.get_xaxis().set_visible(False)
            ax2.get_xaxis().set_visible(False)
            
    def plot(self):
        """ The plot method. Following is only important for the anotate text. If the solvent==H$_2$O the pH value should also be showed"""
        if self.e_chem.experiments[self.experiment_list[0]].electrolyte.solvent=="H$_2$O":
            annotate_text=f"{self.e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration} {self.e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration_unit} {self.e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt} {self.e_chem.experiments[self.experiment_list[0]].electrolyte.solvent} pH={self.e_chem.experiments[self.experiment_list[0]].electrolyte.pH} \n$J$={self.induced_current_density} {self.induced_current_density_unit}"
        else:
            annotate_text=f"{self.e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration} {self.e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration_unit} {self.e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt} {self.e_chem.experiments[self.experiment_list[0]].electrolyte.solvent} \n$J$={self.induced_current_density}  {self.induced_current_density_unit}"
        def interactive(xlabel=self.xlabel, ylabel=self.ylabel,savename="CP_plot.pdf",xcoord=0.55,ycoord=0.05,annotate_text=widgets.Textarea(value=annotate_text),save=False,annotate=True,legend=True):
            fig, ax = plt.subplots() 
            for experiment in self.experiment_list:
                ax.plot(self.df_liste[experiment]["t"], self.df_liste[experiment]["E"],label=self.e_chem.experiments[experiment].name)
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            if legend:
                ax.legend(loc="best",frameon=False)
            if annotate:
                ax.annotate(annotate_text,xy=(xcoord,ycoord),xycoords="axes fraction")
            if save:
                fig.savefig("plots/" + savename,bbox_inches='tight')
        widgets.interact(interactive,xcoord=(0,1.2,0.05),ycoord=(0,1.2,0.05))

    def end_value(self):
        def interactive(xlabel=self.xlabel, ylabel=self.ylabel,savename="CP_plot.pdf",last_points=100,save=False,last_points_line=False):
            names=[]
            end_values=[] 
            average_list=[]
            fig,ax =plt.subplots()
            """ Interactive button"""
            def on_button_click(_):
                for experiment in self.experiment_list:
                    end_potential=lib.PotentialEndValue(method="average over last values",end_value=end_values[experiment],last_average_points=last_points,change_reference_potential=self.delta_E,reference_name=self.reference_name)
                    self.e_chem.experiments[experiment].analysis.cp.potential_end_value.append(end_potential)
                    print(end_potential)
                print("Potential was added to the datamodel")
            button = widgets.Button(description="Save potential")
            for experiment in self.experiment_list:
                last_values = self.df_liste[experiment].tail(last_points)["E"].values[0]
                average = last_values.mean()
                average_list.append(average)
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
                print(average)
                #print(experiment)
                ax.plot(self.df_liste[experiment]["t"], self.df_liste[experiment]["E"],label=self.e_chem.experiments[experiment].name)
                ax.plot(self.df_liste[experiment]["t"], [average] * len(self.df_liste[experiment]["t"]), linewidth=3,linestyle='dotted', label="{} average".format(self.e_chem.experiments[experiment].name))
                ax.legend(loc="best",frameon=False)
                
                if last_points_line:
                    ax.axvline(x=self.df_liste[experiment].tail(last_points)["t"].values[0], color='black', linestyle='--', label="last points")

                names.append(self.e_chem.experiments[experiment].name)
                end_values.append(average) 
                if save:
                    fig.savefig("plots/" + savename,bbox_inches='tight') 
            button.on_click(on_button_click)
            display(button)
            self.end_value_df = pd.DataFrame(list(zip(names,end_values)), columns=["Name",f"Average of the last {last_points} points"]) 
      
            return  self.end_value_df
        widgets.interact(interactive,last_points=(1,400))
    def end_value_fit(self):
        def exponential_fit(x, a, b, c):
            return a * np.exp(-b/2 * x) + c
        names=[]
        end_values=[]
        def interactive(xlabel=self.xlabel, ylabel=self.ylabel,savename="CA_plot.pdf",save=False):
            fig,ax =plt.subplots()
            def on_button_click(_):
                for experiment in self.experiment_list:
                    end_potential=lib.PotentialEndValue(method="Fit function",fit_function="a*exp(-b/2 * x)+ c",end_value=end_values[experiment],change_reference_potential=self.delta_E,reference_name=self.reference_name)
                    self.e_chem.experiments[experiment].analysis.cp.potential_end_value.append(end_potential)
                    print(end_potential)
                print("Potential was added to the datamodel")
            button = widgets.Button(description="Save potential")
            for experiment in self.experiment_list:
                t_fit = np.linspace(0, self.df_liste[experiment]["t"].max(), self.df_liste[experiment].shape[0])
                popt, pcov = curve_fit(exponential_fit,self.df_liste[experiment]["t"], self.df_liste[experiment]["E"])
                c=popt[2]
                names.append(self.e_chem.experiments[experiment].name)
                end_values.append(c)
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
                ax.plot(self.df_liste[experiment]["t"], self.df_liste[experiment]["E"],label=self.e_chem.experiments[experiment].name)
                ax.plot(t_fit, exponential_fit(t_fit, *popt),linewidth=3,linestyle='dotted', label="{} fit".format(self.e_chem.experiments[experiment].name))
                ax.legend(loc="best",frameon=False)
                if save:
                    fig.savefig("plots/" + savename,bbox_inches='tight')
                self.end_value_fit_df = pd.DataFrame(list(zip(names,end_values)), columns=["Name","End value"])
            button.on_click(on_button_click)
            display(button)   
            return  self.end_value_fit_df
        widgets.interact(interactive)

class Chronoamperometry:
    def __init__(self,e_chem,experiment_list,current_density=False):
        self.e_chem = e_chem
        self.induced_potential= self.e_chem.experiments[experiment_list[0]].analysis.ca.induced_potential[0]
        
        self.experiment_list=experiment_list
        self.df_liste=[]
        self.xlabel=f"$t$ ({self.e_chem.experiments[experiment_list[0]].analysis.ca.measurement_time_unit})"
        self.ylabel=f"$I$ ({self.e_chem.experiments[experiment_list[0]].analysis.ca.measurement_current_unit})" 
        mapping_dict={"cm^2":"cm$^2$",
                      "mm^2":"mm$^2$"}
        area_unit=mapping_dict[self.e_chem.experiments[experiment_list[0]].electrode_setup.working_electrode_area_unit]
        for experiment in range(0,len(self.e_chem.experiments)):
            if self.e_chem.experiments[experiment].type=="CA" and self.e_chem.experiments[experiment].filename.endswith(".dat"):
                df = pd.read_csv(self.e_chem.experiments[experiment].filename, sep="\s", header=0, names=["t", "I"],engine="python")
                self.df_liste.append(df)
            elif self.e_chem.experiments[experiment].type=="CA" and self.e_chem.experiments[experiment].filename.endswith(".txt"):
                df=pd.read_csv(self.e_chem.experiments[experiment].filename,header=0,sep=";",decimal=',',usecols=[0,2],names=["t","I"])
                self.df_liste.append(df)
            elif self.e_chem.experiments[experiment].type=="CA" and self.e_chem.experiments[experiment].filename.endswith(".csv"):
                df = pd.read_csv(self.e_chem.experiments[experiment].filename, sep=",", header=4, skipfooter=1, names=["t", "I"])
                self.df_liste.append(df)
            else:
                self.df_liste.append(None)
                pass 
        if current_density:
            self.ylabel=f"$J$ ({self.e_chem.experiments[experiment_list[0]].analysis.ca.measurement_current_unit}/{area_unit})"
            for df in self.df_liste:
                if df is not None:
                    for experiment in range(len(self.e_chem.experiments)):
                        df["I"] = df["I"] / self.e_chem.experiments[experiment].electrode_setup.working_electrode_area

    def plot(self):
        if self.e_chem.experiments[self.experiment_list[0]].electrolyte.solvent=="H$_2$O":
            annotate_text=f"{self.e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration} {self.e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration_unit} {self.e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt} {self.e_chem.experiments[self.experiment_list[0]].electrolyte.solvent} pH={self.e_chem.experiments[self.experiment_list[0]].electrolyte.pH} \n$E$={self.e_chem.experiments[self.experiment_list[0]].analysis.ca.induced_potential[0]} {self.e_chem.experiments[self.experiment_list[0]].analysis.ca.induced_potential_unit}"
        else:
            annotate_text=f"{self.e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration} {self.e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration_unit} {self.e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt} {self.e_chem.experiments[self.experiment_list[0]].electrolyte.solvent}  \n$E$={self.e_chem.experiments[self.experiment_list[0]].analysis.ca.induced_potential[0]} {self.e_chem.experiments[self.experiment_list[0]].analysis.ca.induced_potential_unit}"
        def interactive(xlabel=self.xlabel, ylabel=self.ylabel,savename="CA_plot.pdf",xcoord=0.55,ycoord=0.05,annotate_text=widgets.Textarea(value=annotate_text),save=False,annotate=True,legend=True):
            fig, ax = plt.subplots() 
            for experiment in self.experiment_list:
                ax.plot(self.df_liste[experiment]["t"], self.df_liste[experiment]["I"], label=self.e_chem.experiments[experiment].name)

            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            if legend:
                ax.legend(loc="best",frameon=False)
            if save:
                fig.savefig("plots/" + savename,savename,bbox_inches='tight')
            if annotate:
                ax.annotate(annotate_text,xy=(xcoord,ycoord),xycoords="axes fraction")
        widgets.interact(interactive,xcoord=(0,1.2,0.05),ycoord=(0,1.2,0.05))
    def end_value_fit(self):
        def exponential_fit(x, a, b, c):
            return a * np.exp(-b/2 * x) + c
        names=[]
        end_values=[]
        def interactive(xlabel=self.xlabel, ylabel=self.ylabel,savename="CA_plot.pdf",save=False):
            fig,ax =plt.subplots()
            for experiment in self.experiment_list:
                t_fit = np.linspace(0, self.df_liste[experiment]["t"].max(), self.df_liste[experiment].shape[0])
                popt, pcov = curve_fit(exponential_fit,self.df_liste[experiment]["t"], self.df_liste[experiment]["I"])
                c=popt[2]
                names.append(self.e_chem.experiments[experiment].name)
                end_values.append(c)
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
                ax.plot(self.df_liste[experiment]["t"], self.df_liste[experiment]["I"],label=self.e_chem.experiments[experiment].name)
                ax.plot(t_fit, exponential_fit(t_fit, *popt),linewidth=3,linestyle='dotted', label="{} fit".format(self.e_chem.experiments[experiment].name))
                ax.legend(loc="best",frameon=False)
                if save:
                    fig.savefig("plots/" + savename,bbox_inches='tight')
                self.end_value_fit_df = pd.DataFrame(list(zip(names,end_values)), columns=["Name","End value"])   
            return  self.end_value_fit_df
        widgets.interact(interactive)
    def end_value(self):
        def interactive(xlabel=self.xlabel, ylabel=self.ylabel,savename="CA_plot.pdf",last_points=75,save=False):
            names=[]
            end_values=[] 
            fig,ax =plt.subplots()
            for experiment in self.experiment_list:
                last_values = self.df_liste[experiment].tail(last_points)["I"].values[0]
                average = last_values.mean()
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
                ax.plot(self.df_liste[experiment]["t"], self.df_liste[experiment]["I"],label=self.e_chem.experiments[experiment].name)
                ax.plot(self.df_liste[experiment]["t"], [average] * len(self.df_liste[experiment]["t"]), linewidth=3,linestyle='dotted', label="{} average".format(self.e_chem.experiments[experiment].name))
                ax.legend(loc="best",frameon=False)
                names.append(self.e_chem.experiments[experiment].name)
                end_values.append(average) 
                if save:
                    fig.savefig("plots/" + savename,bbox_inches='tight') 
            self.end_value_df = pd.DataFrame(list(zip(names,end_values)), columns=["Name", f"Average of the last {last_points} points"]) 
            return  self.end_value_df
        widgets.interact(interactive,last_points=(1,200))

class CyclicVoltammetry:
    def __init__(self,e_chem,experiment,cycles=None,change_reference_list_index=None,current_density=False,change_reference=False):
        self.e_chem=e_chem
        if self.e_chem.experiments[experiment].type=="CV"  and self.e_chem.experiments[experiment].filename.endswith(".csv"):
            self.df = pd.read_csv(self.e_chem.experiments[experiment].filename,header=5,skipfooter=1,engine="python")#
        elif self.e_chem.experiments[experiment].type=="CV"  and self.e_chem.experiments[experiment].filename.endswith(".xlsx"):
            self.df=pd.read_excel(self.e_chem.experiments[experiment].filename,header=1)
        else:
            print("This is not a CV data")  
        """ Determination of all cycles in the file"""
        self.total_cycles=len(self.df.columns) // 2
        self.all_cycles_list= [i for i in range(1,self.total_cycles+1)]
        """ Accepts the cycle list if it is None than it uses all cycles"""
        self.cycles= cycles if cycles is not None else self.all_cycles_list
        """Information for the plots """
        self.electrolyte= f"{self.e_chem.experiments[experiment].electrolyte.conducting_salt_concentration} {self.e_chem.experiments[experiment].electrolyte.conducting_salt_concentration_unit} {self.e_chem.experiments[experiment].electrolyte.conducting_salt} {self.e_chem.experiments[experiment].electrolyte.solvent}"
        self.name= self.e_chem.experiments[experiment].name 
        self.substrate= self.e_chem.experiments[experiment].electrode_setup.working_electrode
        self.scan_rate= f"{self.e_chem.experiments[experiment].analysis.cv.scan_rate} {self.e_chem.experiments[experiment].analysis.cv.scan_rate_unit}"
        self.mapping_dict_reference_names={"SHE":"SHE",
                      "RHE":"RHE",
                      "Hg/Hg2Cl2": "Hg/Hg$_2$Cl$_2$",
                      "Ag/AgCl":"Ag/AgCl",
                      "Ag/Ag2SO4": "Ag/Ag$_2$SO$_4$",
                      "Hg/HgO": "Hg/HgO",
                      "Hg/Hg2SO4":"Hg/Hg$_2$SO$_4$",
                      "Fc/Fc+": "Fc/Fc$^{+}"}
        self.reference_name=self.e_chem.experiments[experiment].electrode_setup.reference_electrode
        self.reference = self.mapping_dict_reference_names[self.e_chem.experiments[experiment].electrode_setup.reference_electrode]
        mapping_dict={"cm^2":"cm$^2$",
                      "mm^2":"mm$^2$"}
        area_unit=mapping_dict[self.e_chem.experiments[experiment].electrode_setup.working_electrode_area_unit]
        self.E = ["E" for i in range(self.total_cycles)]
        self.I = ["I" for i in range(self.total_cycles)]
        self.df.columns = [name for pair in zip(self.E, self.I) for name in pair]
        self.num_cycles = int(self.df.shape[1] / 2)
        self.cycle_df = np.array_split(self.df, self.num_cycles, axis=1)
        self.cycles = [cycle -1 for cycle in self.cycles]
        self.experiment=experiment
        self.xunit=f"{self.e_chem.experiments[experiment].analysis.cv.measurement_potential_unit}"
        self.yunit=f"{self.e_chem.experiments[experiment].analysis.cv.measurement_current_unit}"
        mapping_dict_reference_names={"SHE":"SHE",
                      "RHE":"RHE",
                      "Hg/Hg2Cl2": "Hg/Hg$_2$Cl$_2$",
                      "Ag/AgCl":"Ag/AgCl",
                      "Hg/HgO": "Hg/HgO",
                      "Fc/Fc+": "Fc/Fc$^{+}"}
        if change_reference:
            self.delta_E=self.e_chem.experiments[experiment].analysis.cv.change_potential[change_reference_list_index][0]
            self.reference=mapping_dict_reference_names[self.e_chem.experiments[experiment].analysis.cv.change_potential[change_reference_list_index][1]]
            self.reference_name=self.e_chem.experiments[experiment].analysis.cv.change_potential[change_reference_list_index][1]
            self.ylabel=f"$E$ vs. {self.reference} ({self.e_chem.experiments[experiment].analysis.cv.measurement_potential_unit})"
            for df in  self.cycle_df:
                    df['E'] = df['E'] + self.delta_E
        else:
            self.delta_E = 0
        self.xlabel= f"$E$ vs. {self.reference} ({self.e_chem.experiments[experiment].analysis.cv.measurement_potential_unit})"
        self.ylabel= f"$I$ ({self.e_chem.experiments[experiment].analysis.cv.measurement_current_unit})"
        if current_density:
            self.ylabel=f"$J$ ({self.e_chem.experiments[experiment].analysis.cv.measurement_current_unit}/{area_unit})"
            self.yunit=f"{self.e_chem.experiments[experiment].analysis.cv.measurement_current_unit}/{self.e_chem.experiments[experiment].electrode_setup.working_electrode_area_unit}"
            for df in self.cycle_df:
                df["I"] = df["I"] / self.e_chem.experiments[experiment].electrode_setup.working_electrode_area
        if len(e_chem.experiments[experiment].analysis.cv.cycles) == 0:
            for cycle in self.all_cycles_list:
                Cycle = lib.Cycle(number=cycle)
                e_chem.experiments[experiment].analysis.cv.cycles.append(Cycle)
        # Determination of the lowest/highest current for the zoom option in the plot method
        max_value = -np.inf  
        min_value = np.inf         
        for i in self.cycles:
            current_max = np.max(self.cycle_df[i]["I"])
            current_min = np.min(self.cycle_df[i]["I"])
            potential_max = np.max(self.cycle_df[i]["E"])
            potential_min = np.min(self.cycle_df[i]["E"])
            self.max_current_value = max(max_value,current_max)
            self.min_current_value= min(min_value,current_min)
            self.max_potential_value = max(max_value,potential_max)
            self.min_potential_value= min(min_value,potential_min)
            self.min_current_value -= 2
            self.max_current_value += 2
    def plot(self):
        xlabel=self.xlabel
        ylabel=self.ylabel
        if self.e_chem.experiments[self.experiment].electrolyte.solvent=="H$_2$O":
            annotate_text=f"{self.electrolyte}/pH={self.e_chem.experiments[self.experiment].electrolyte.pH}/{self.substrate}\n$v$={self.scan_rate}"
        else:
            annotate_text=f"{self.electrolyte}/{self.substrate}\n$v$={self.scan_rate}"
        def interactive(xlabel=xlabel, ylabel=ylabel,savename="CV_plot.pdf",text_xcoord=0.55,text_ycoord=0.05,annotate_text=widgets.Textarea(value=annotate_text),save=False,annotate=False,legend=True,arrow=True,y_arrow_position=self.cycle_df[0]['I'][0]+1, arrow_width=1,arrow_end=15,zoom_x=False,zoom_x_min=self.cycle_df[0]['E'].min()-0.1,zoom_x_max=self.cycle_df[0]['E'].max()+0.1,zoom_y=False,zoom_y_min=self.min_current_value,zoom_y_max=self.max_current_value): 
            fig, ax = plt.subplots()
            for i in self.cycles: 
                ax.plot(self.cycle_df[i]["E"],self.cycle_df[i]["I"],label="Cycle: {}".format(i+1))
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
            if legend:
                ax.legend(loc="best",frameon=False)
            if annotate:
                ax.annotate(annotate_text, xy=(text_xcoord,text_ycoord), xycoords="axes fraction")
            if arrow:
                self.cycle_df[0]['E'] = self.cycle_df[0]['E'].astype(float)
                self.cycle_df[0]['I'] = self.cycle_df[0]['I'].astype(float)
                ax.arrow(self.cycle_df[0]['E'][0],y_arrow_position, dx=self.cycle_df[0]['E'][arrow_end]-self.cycle_df[0]['E'][0], dy=0, head_width=(self.max_current_value-self.min_current_value)/30*arrow_width, head_length=(self.cycle_df[0]['E'].max()-self.cycle_df[0]['E'].min())/12, fc='black', ec='black')
            if zoom_x:
                ax.set_xlim(zoom_x_min,zoom_x_max)
            if zoom_y:
                ax.set_ylim(zoom_y_min,zoom_y_max)
            if save:
                fig.savefig("plots/" + savename,bbox_inches='tight')
        widgets.interact(interactive,text_xcoord=(0,1.2,0.05),text_ycoord=(0,1.2,0.05),y_arrow_position=(self.cycle_df[0]['I'].min(),self.cycle_df[0]['I'].max()),arrow_width=(0.1,5,0.5),arrow_end=(1,100,1),zoom_x_min=(self.cycle_df[0]['E'].min()-0.1,self.cycle_df[0]['E'].max()+0.1),zoom_x_max=(self.cycle_df[0]['E'].min()-0.1,self.cycle_df[0]['E'].max()+0.1),zoom_y_min=(self.min_current_value,self.max_current_value),zoom_y_max=(self.min_current_value,self.max_current_value))
    def peaks(self):
        x_max = self.cycle_df[0]['E'].max()
        x_min = self.cycle_df[0]['E'].min()
        xlabel=self.xlabel
        ylabel=self.ylabel
        def interactive(E_Min=x_min,E_Max=x_max,vertex_line=False,savename="CV_peaks.pdf",save=False,zoom_x=False,zoom_x_min=self.cycle_df[0]['E'].min()-0.1,zoom_x_max=self.cycle_df[0]['E'].max()+0.1,zoom_y=False,zoom_y_min=self.min_current_value,zoom_y_max=self.max_current_value): 
            E_min=[]
            E_max=[]
            E_hwp=[]
            Cycles=[]
            I_max=[]
            I_min=[]
            I_vertex_list=[]
            for cycle in self.cycles:
            # Here are interactive buttons, which allowing to save the peaks to the data model
                def on_button_click_min(_):
                    for cycle in self.cycles:
                        min_peak=lib.PeaksAndHalfPotential(current_minimum=I_min[cycle],y_unit=f"{self.yunit}",potential_minimum=E_min[cycle],change_reference_potential=self.delta_E,reference_name=self.reference_name)
                        self.e_chem.experiments[self.experiment].analysis.cv.cycles[cycle].peaks_and_half_potential.append(min_peak)
                        print(min_peak)
                    print("Minimum peak was added to the datamodel")
                button_min = widgets.Button(description="Save only Minimum")
                def on_button_click_max(_):
                    for cycle in self.cycles:
                        max_peak=lib.PeaksAndHalfPotential(current_maximum=I_max[cycle],y_unit=f"{self.yunit}",potential_maximum=I_max[cycle],change_reference_potential=self.delta_E,reference_name=self.reference_name)
                        self.e_chem.experiments[self.experiment].analysis.cv.cycles[cycle].peaks_and_half_potential.append(max_peak)
                        print(max_peak)
                    print("Maximum Saved")
                button_max = widgets.Button(description="Save only Maximum")
                def on_button_click_hwp(_):
                    for cycle in self.cycle_df:
                        peaks_and_hwp=lib.PeaksAndHalfPotential(current_minimum=I_min[cycle],potential_minimum=E_min[cycle],current_maximum=I_max[cycle],y_unit=f"{self.yunit}",potential_maximum=E_max[cycle],change_reference_potential=self.delta_E,half_wave_potential=E_hwp[cycle],reference_name=self.reference_name)
                        self.e_chem.experiments[self.experiment].analysis.cv.cycles[cycle].peaks_and_half_potential.append(peaks_and_hwp)
                        print(peaks_and_hwp)
                    print("Peaks and half-wave potential Saved")
                button_hwp = widgets.Button(description="Save Peaks and HWP")
                # Following is for the plot
                fig, ax=plt.subplots()
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
                if zoom_x:
                    ax.set_xlim(zoom_x_min,zoom_x_max)
                if zoom_y:
                    ax.set_ylim(zoom_y_min,zoom_y_max)
                ax.plot(self.cycle_df[cycle]["E"],self.cycle_df[cycle]["I"],label="Cycle: {}".format(cycle+1))
                Cycles.append("Cycle: {}".format(cycle+1))
                # The range for the peak seach
                indices = np.where((self.cycle_df[cycle]["E"] >= E_Min) & (self.cycle_df[cycle]["E"] <= E_Max))[0]
                max_index = indices[np.argmax(self.cycle_df[cycle]["I"][indices])]
                pot_at_max = self.cycle_df[cycle]["E"][max_index]
                current_at_max = self.cycle_df[cycle]["I"][max_index]
                min_index = indices[np.argmin(self.cycle_df[cycle]["I"][indices])]
                pot_at_min = self.cycle_df[cycle]["E"][min_index]
                current_at_min = self.cycle_df[cycle]["I"][min_index]
                max_E= np.argmax(self.cycle_df[cycle]["E"])
                min_E= np.argmin(self.cycle_df[cycle]["E"])
                I_at_max_E=self.cycle_df[cycle]["I"][max_E]
                I_at_min_E=self.cycle_df[cycle]["I"][min_E]
                I_start=self.cycle_df[cycle]["I"][0]
                """ Lines for the peaks and half-wave potential"""
                ax.axvline(x=(pot_at_max+pot_at_min)/2 , color='red', linestyle='--',linewidth=2)
                ax.axvline(x=pot_at_min , color='darkgreen', linestyle=':',linewidth=2)
                ax.axvline(x=pot_at_max , color='orange', linestyle=':')
                """ The legend"""
                ax.legend(frameon=False)
                """ Adding vertex to cycles"""
                if self.cycle_df[0]["E"][0]< self.cycle_df[0]["E"][10]:
                    I_vertex=I_at_max_E
                    E_vertex=self.cycle_df[cycle]["I"][max_E]
                    self.e_chem.experiments[self.experiment].analysis.cv.cycles[cycle].potential_vertex= E_vertex
                    self.e_chem.experiments[self.experiment].analysis.cv.cycles[cycle].current_vertex=I_vertex
                    self.e_chem.experiments[self.experiment].analysis.cv.cycles[cycle].y_unit=f"{self.yunit}"
                    self.e_chem.experiments[self.experiment].analysis.cv.cycles[cycle].change_reference_potential=self.delta_E
                    self.e_chem.experiments[self.experiment].analysis.cv.cycles[cycle].reference_name=self.reference_name

                else:
                    I_vertex=I_at_min_E
                    E_vertex=self.cycle_df[cycle]["I"][min_E]
                    self.e_chem.experiments[self.experiment].analysis.cv.cycles[cycle].potential_vertex= E_vertex
                    self.e_chem.experiments[self.experiment].analysis.cv.cycles[cycle].current_vertex=I_vertex
                    self.e_chem.experiments[self.experiment].analysis.cv.cycles[cycle].y_unit=f"{self.yunit}"
                    self.e_chem.experiments[self.experiment].analysis.cv.cycles[cycle].change_reference_potential=self.delta_E
                    self.e_chem.experiments[self.experiment].analysis.cv.cycles[cycle].reference_name=self.reference_name
                """ Adding values to list"""
                E_max.append(pot_at_max)
                E_min.append(pot_at_min)
                hwp=(pot_at_max+pot_at_min)/2
                E_hwp.append(hwp)
                average_hwp = np.average(E_hwp)
                I_min.append(current_at_min)
                I_max.append(current_at_max)
                I_vertex_list.append(I_vertex)
                if vertex_line:
                    ax.axhline(y=I_vertex , color='black', linestyle='-') 
            Cycles.append("Average")
            E_hwp.append(average_hwp)
            I_min.append(np.average(I_min))
            I_max.append(np.average(I_max))
            E_min.append(np.average(E_min))
            E_max.append(np.average(E_max))
            I_vertex_list.append(np.average(I_vertex_list))
            button_min.on_click(on_button_click_min)
            display(button_min)
            button_max.on_click(on_button_click_max)
            display(button_max)
            button_hwp.on_click(on_button_click_hwp)
            display(button_hwp)
            self.df_peaks = pd.DataFrame(list(zip(Cycles,E_min,I_min,E_max,I_max,E_hwp,I_vertex_list)), columns=["Cycles",'E_at_min',"I min",'E_at_max',"I max","E1/2","I_vertex"]) 
            if save:
                fig.savefig("plots/" +"Cycle{}_".format(cycle+1)+savename,bbox_inches='tight')

            return self.df_peaks
        widgets.interact(interactive,E_Min=(x_min,x_max),E_Max=(x_min,x_max),zoom_x_min=(self.cycle_df[0]['E'].min()-0.1,self.cycle_df[0]['E'].max()+0.1),zoom_x_max=(self.cycle_df[0]['E'].min()-0.1,self.cycle_df[0]['E'].max()+0.1),zoom_y_min=(self.min_current_value,self.max_current_value),zoom_y_max=(self.min_current_value,self.max_current_value))
        
        return 
    def integration(self):
        x_max = self.cycle_df[0]['E'].max()
        x_min = self.cycle_df[0]['E'].min()
        xlabel=self.xlabel
        ylabel=self.ylabel
        def interactive(E_min=(x_min-0.1,x_max,0.01),E_max=(x_min,x_max,0.01),E_min_back=(x_min-0.1,x_max,0.01),E_max_back=(x_min,x_max,0.01),savename="integration.pdf",save=False,zoom_x=False,zoom_x_min=self.cycle_df[0]['E'].min()-0.1,zoom_x_max=self.cycle_df[0]['E'].max()+0.1,zoom_y=False,zoom_y_min=self.min_current_value,zoom_y_max=self.max_current_value):
            Cycles=[]
            Integral_forward=[]
            Integral_backward=[]
            for i in self.cycles:
                    # Interactive Buttons
                    def on_button_click_forward(_):
                        Peak=lib.PeakIntegration(lower_limit_potential=E_min,upper_limit_potential=E_max,integration_area=area_forward,integration_area_unit=f"{self.yunit}*{self.xunit}",integration_direction="Forward")
                        self.e_chem.experiments[self.experiment].analysis.cv.cycles[i].peak_integration.append(Peak)
                        print(self.e_chem.experiments[self.experiment].analysis.cv.cycles[i].peak_integration)
                        print("Forward Integration Saved")
                    # For the plot
                    button_forward = widgets.Button(description="ForwardArea2Model")
                    def on_button_click_backward(_):
                        Peak=lib.PeakIntegration(lower_limit_potential=E_min,upper_limit_potential=E_max,integration_area=area_forward,integration_direction="Backward")
                        self.e_chem.experiments[self.experiment].analysis.cv.cycles[i].peak_integration.append(Peak)
                        print(self.e_chem.experiments[self.experiment].analysis.cv.cycles[i].peak_integration)
                        print("Backward Integration Saved")
                    # For the plot
                    button_backward = widgets.Button(description="BackwardArea2Model")
                    Cycles.append("Cycle: {}".format(i+1)) 
                    fig,ax=plt.subplots()
                    if zoom_x:
                        ax.set_xlim(zoom_x_min,zoom_x_max)
                    if zoom_y:
                        ax.set_ylim(zoom_y_min,zoom_y_max)
                    # Split a Cycle into forward and backward
                    df=self.cycle_df[i]
                    half= len(df)//2
                    forward_cycle=df.iloc[:half,:]
                    backward_cycle=df.iloc[half:,:]
                    forward_cycle_peak = forward_cycle[(forward_cycle['E'] >= E_min) & (forward_cycle['E'] <= E_max)]
                    #new regression
                    start_value = forward_cycle_peak.iloc[0]['E']
                    end_value = forward_cycle_peak.iloc[-1]['E']
                    forward_slope = (forward_cycle_peak.iloc[-1]['I'] - forward_cycle_peak.iloc[0]['I']) / (end_value - start_value)
                    intercept = forward_cycle_peak.iloc[0]['I'] - forward_slope * start_value
                    def line_func(x):
                        return forward_slope * x + intercept
                    y_pred1 = line_func(forward_cycle_peak['E'].values)
                    area_forward = trapz(forward_cycle_peak['I'] - y_pred1.flatten(), forward_cycle_peak['E'])
                    ax.plot(forward_cycle_peak['E'], y_pred1.flatten(),color="black", linestyle='--')
                    #ax.fill_between(forward_cycle_peak['E'], forward_cycle_peak['I'], y_pred1.flatten(), where=(forward_cycle_peak['I'] > y_pred1.flatten()), alpha=0.3)
                    ax.fill_between(forward_cycle_peak['E'], forward_cycle_peak['I'], y_pred1.flatten(), alpha=0.3)
                    backward_cycle_peak = backward_cycle[(backward_cycle['E'] >= E_min_back) & (backward_cycle['E'] <= E_max_back)]
                    start_value_back = backward_cycle_peak.iloc[0]['E']
                    end_value_back = backward_cycle_peak.iloc[-1]['E']
                    backward_slope = (backward_cycle_peak.iloc[-1]['I'] - backward_cycle_peak.iloc[0]['I']) / (end_value_back - start_value_back)
                    intercept_back = backward_cycle_peak.iloc[0]['I'] - backward_slope * start_value_back
                    def line_func_back(x):
                        return backward_slope * x + intercept_back
                    y_pred2 = line_func_back(backward_cycle_peak['E'].values)
                    area_backward = trapz(backward_cycle_peak['I'] - y_pred2.flatten(), backward_cycle_peak['E'])
                    ax.plot(backward_cycle_peak['E'], y_pred2.flatten(), color='black', linestyle='--')
                    ax.fill_between(backward_cycle_peak['E'], backward_cycle_peak['I'], y_pred2.flatten(), where=(backward_cycle_peak['I'] > y_pred2.flatten()), alpha=0.3)
                    backward_cycle_peak = backward_cycle[(backward_cycle['E'] >= E_min_back) & (backward_cycle['E'] <= E_max_back)]
                    start_value_back = backward_cycle_peak.iloc[0]['E']
                    end_value_back = backward_cycle_peak.iloc[-1]['E']
                    backward_slope = (backward_cycle_peak.iloc[-1]['I'] - backward_cycle_peak.iloc[0]['I']) / (end_value_back - start_value_back)
                    intercept_back = backward_cycle_peak.iloc[0]['I'] - backward_slope * start_value_back

                    ax.fill_between(backward_cycle_peak['E'], backward_cycle_peak['I'], y_pred2.flatten(), alpha=0.3)# where=(backward_cycle_peak['I'] < y_pred2.flatten())
   
                    Integral_forward.append(area_forward)
                    Integral_backward.append(area_backward)

                    ax.plot(df["E"],df["I"],label="Cycle: {}".format(i+1))
                    ax.set_xlabel(xlabel)
                    ax.set_ylabel(ylabel)
                    ax.legend(frameon=False)

                    if save:
                        fig.savefig("plots/" +"Cycle{}_".format(i+1)+savename,bbox_inches='tight')

                    self.df_integration= pd.DataFrame(zip(Cycles,Integral_forward,Integral_backward), columns=["Cycles","Integration Area forward","Integration Area backward"])
            button_forward.on_click(on_button_click_forward)
            display(button_forward)
            button_backward.on_click(on_button_click_backward)
            display(button_backward)
            return self.df_integration

        widgets.interact(interactive,zoom_x_min=(self.cycle_df[0]['E'].min()-0.1,self.cycle_df[0]['E'].max()+0.1),zoom_x_max=(self.cycle_df[0]['E'].min()-0.1,self.cycle_df[0]['E'].max()+0.1),zoom_y_min=(self.min_current_value,self.max_current_value),zoom_y_max=(self.min_current_value,self.max_current_value))
    def ferrocene_reference(self,experiment2):
        if self.e_chem.experiments[experiment2].type=="CV"  and self.e_chem.experiments[experiment2].filename.endswith(".csv"):
            self.df2 = pd.read_csv(self.e_chem.experiments[experiment2].filename,header=5,skipfooter=1,engine="python")
        elif self.e_chem.experiments[experiment2].type=="CV"  and self.e_chem.experiments[experiment2].filename.endswith(".xlsx"):
            self.df2=pd.read_excel(self.e_chem.experiments[experiment2].filename,header=1)
        self.total_cycles2=len(self.df2.columns) // 2
        self.all_cycles_list2= [i for i in range(1,self.total_cycles2+1)]
        self.cycles2= self.all_cycles_list2
        self.E2 = ["E" for i in range(self.total_cycles)]
        self.I2 = ["I" for i in range(self.total_cycles)]
        self.df2.columns = [name for pair in zip(self.E2, self.I2) for name in pair]
        self.num_cycles2 = int(self.df2.shape[1] / 2)
        self.cycle_df2 = np.array_split(self.df2, self.num_cycles2, axis=1)
        self.cycles2 = [cycle -1 for cycle in self.cycles2]
        x_max_sec = self.cycle_df2[0]['E'].max()
        x_min_sec = self.cycle_df2[0]['E'].min()

        x_max = self.cycle_df[0]['E'].max()
        x_min = self.cycle_df[0]['E'].min()
        xlabel=self.xlabel
        ylabel=self.ylabel
        def interactive(E_min_Fc=0.2,E_max_Fc=0.6,sample_point= 'half-wave potential',E_min_sample=x_min-0.45,E_max_sample=x_max-0.4,E_min_sec=x_min_sec,E_max_sec=x_max_sec): 
            E_min_ferrocene=[]
            E_max_ferrocene=[]
            E_hwp_ferrocene=[]
            E_min_sample_list=[]
            E_max_sample_list=[]
            E_hwp_sample_list=[]
            E_min_sec_list=[]
            E_max_sec_list=[]
            E_hwp_sec_list=[]
            delta_E_min_list=[]
            delta_E_max_list=[]
            delta_E_hwp_list=[]
            Cycles=[]
            self.cycle_df_ferrocene = copy.deepcopy(self.cycle_df)
            for i in self.cycles:
                fig, ax=plt.subplots()
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
                ax.set_title("measurement without ferrocene calibration ")
                ax.plot(self.cycle_df[i]["E"],self.cycle_df[i]["I"],label="Cycle: {}".format(i+1))
                Cycles.append("Cycle: {}".format(i+1))
                indices = np.where((self.cycle_df[i]["E"] >= E_min_Fc) & (self.cycle_df[i]["E"] <= E_max_Fc))[0]
                max_index = indices[np.argmax(self.cycle_df[i]["I"][indices])]
                pot_at_max = self.cycle_df[i]["E"][max_index]
                current_at_max = self.cycle_df[i]["I"][max_index]
                min_index = indices[np.argmin(self.cycle_df[i]["I"][indices])]
                pot_at_min = self.cycle_df[i]["E"][min_index]
                current_at_min = self.cycle_df[i]["I"][min_index]
                ax.axvline(x=(pot_at_max+pot_at_min)/2 , color='red', linestyle='--',linewidth=2)
                ax.axvline(x=pot_at_min , color='darkgreen', linestyle=':',linewidth=2)
                ax.axvline(x=pot_at_max , color='orange', linestyle=':')
                ax.legend(frameon=False)
                E_max_ferrocene.append(pot_at_max)
                E_min_ferrocene.append(pot_at_min)
                E_hwp_ferrocene.append((pot_at_max+pot_at_min)/2 )
            for i in range(len(self.cycle_df_ferrocene)):
                if i in self.cycles:
                    self.cycle_df_ferrocene[i]['E'] = self.cycle_df_ferrocene[i]['E'] - ((pot_at_max + pot_at_min) / 2)
            for i in self.cycles:
                fig, ax=plt.subplots()
                ax.set_xlabel("$E$ vs. Fc/Fc$^+$ (V)")
                ax.set_ylabel(ylabel)
                ax.set_title("measurement with ferrocene calibration ")
                ax.plot(self.cycle_df_ferrocene[i]["E"],self.cycle_df_ferrocene[i]["I"],label="Cycle: {}".format(i+1))
                ax.legend(frameon=False)
                indices_sample = np.where((self.cycle_df_ferrocene[i]["E"] >= E_min_sample) & (self.cycle_df_ferrocene[i]["E"] <= E_max_sample))[0]
                max_index_sample = indices_sample[np.argmax(self.cycle_df_ferrocene[i]["I"][indices_sample])]
                pot_at_max_sample = self.cycle_df_ferrocene[i]["E"][max_index_sample]
                current_at_max_sample = self.cycle_df_ferrocene[i]["I"][max_index_sample]
                min_index_sample = indices_sample[np.argmin(self.cycle_df_ferrocene[i]["I"][indices_sample])]
                pot_at_min_sample = self.cycle_df_ferrocene[i]["E"][min_index_sample]
                current_at_min_sample = self.cycle_df_ferrocene[i]["I"][min_index_sample]
                E_max_sample_list.append(pot_at_max_sample)
                E_min_sample_list.append(pot_at_min_sample)
                E_hwp_sample_list.append((pot_at_max_sample+pot_at_min_sample)/2 )
                if sample_point=='half-wave potential':
                    ax.axvline(x=(pot_at_max_sample+pot_at_min_sample)/2 , color='red', linestyle='--',linewidth=2)
                    
                if sample_point=='peak minimum':
                    ax.axvline(x=pot_at_min_sample , color='darkgreen', linestyle=':',linewidth=2)
                if sample_point=='peak maximum':
                    ax.axvline(x=pot_at_max_sample , color='orange', linestyle=':')
            
            for i in self.cycles:
                fig, ax=plt.subplots()
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
                ax.set_title("Second measurement")
                ax.plot(self.cycle_df2[i]["E"],self.cycle_df2[i]["I"],label="Cycle: {}".format(i+1))
                ax.legend(frameon=False)
                indices_sec = np.where((self.cycle_df2[i]["E"] >= E_min_sec) & (self.cycle_df2[i]["E"] <= E_max_sec))[0]
                max_index_sec = indices_sec[np.argmax(self.cycle_df2[i]["I"][indices_sec])]
                pot_at_max_sec = self.cycle_df2[i]["E"][max_index_sec]
                #current_at_max_sec = self.cycle_df2[i]["I"][max_index_sec]
                min_index_sec = indices_sec[np.argmin(self.cycle_df2[i]["I"][indices_sec])]
                pot_at_min_sec = self.cycle_df2[i]["E"][min_index_sec]
                #current_at_min_sec = self.cycle_df2[i]["I"][min_index_sec]
                E_max_sec_list.append(pot_at_max_sec)
                E_min_sec_list.append(pot_at_min_sec)
                E_hwp_sec_list.append((pot_at_max_sec+pot_at_min_sec)/2 )
                delta_E_min_list.append(pot_at_min_sec-pot_at_min_sample)
                delta_E_max_list.append(pot_at_max_sec-pot_at_max_sample)
                delta_E_hwp_list.append(((pot_at_max_sec+pot_at_min_sec)/2)-((pot_at_max_sample+pot_at_min_sample)/2))
                if sample_point=='half-wave potential':
                    ax.axvline(x=(pot_at_max_sec+pot_at_min_sec)/2 , color='red', linestyle='--',linewidth=2)
                if sample_point=='peak minimum':
                    ax.axvline(x=pot_at_min_sec , color='darkgreen', linestyle=':',linewidth=2)
                if sample_point=='peak maximum':
                    ax.axvline(x=pot_at_max_sec , color='orange', linestyle=':')
            if sample_point=='peak minimum':
                self.df_reference = pd.DataFrame(list(zip(Cycles,E_min_sample_list,E_min_sec_list,delta_E_min_list)), columns=["Cycles ","E_at_min/Fc measurement","E_at_min/without Fc","Delta_E"])
            if sample_point=='peak maximum':
                print("peak max")
                self.df_reference = pd.DataFrame(list(zip(Cycles,E_max_sample_list,E_max_sec_list,delta_E_max_list)), columns=["Cycles","E_at_max/Fc measurement","E_at_max/Fc measurement/without Fc","Delta_E"])
            if sample_point=='half-wave potential':
                self.df_ferrocene_reference = pd.DataFrame(list(zip(Cycles,E_hwp_sample_list,E_hwp_sec_list,delta_E_hwp_list)), columns=["Cycles","E1/2/Fc measurement","E1/2/without Fc measurement","Delta_E"])
            return self.df_ferrocene_reference
        widgets.interact(interactive,E_min_Fc=(x_min,x_max,0.05),E_max_Fc=(x_min,x_max,0.05),E_min_sample=(x_min-0.45,x_max-0.4,0.05),E_max_sample=(x_min-0.45,x_max-0.3,0.05),E_min_sec=(x_min_sec,x_max_sec,0.05),E_max_sec=(x_min_sec,x_max_sec,0.05),sample_point= ['peak minimum', 'peak maximum', 'half-wave potential'])
