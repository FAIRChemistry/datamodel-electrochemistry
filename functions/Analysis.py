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
# path_program=os.getcwd()
# print(path_program)

lib = DataModel.from_markdown("specifications/Electrochemistry.md")
e_chem=lib.Dataset()
class ReferenceCalculator:
    def __init__(self):
        self.reference_values = {
            "SHE": 0, 
            "RHE": -0.0592, 
            "Calomel (sat. KCl)": 0.241,
            "Calomel (3.5 M KCl)": 0.250,
            "Calomel (1 M KCl)": 0.280,
            "Calomel (0.1 M KCl)": 0.334,
            "Ag/AgCl (sat. KCl)": 0.199,
            "Ag/AgCl (3.5 M KCl)": 0.205,
            "Hg/HgO (1 M KOH)": 0.140,
            "Hg/HgO (0.1 M KOH)": 0.165,
            "Fc/Fc+": 0.400
        }
        self.table = [[old_reference, new_reference] for old_reference, new_reference in self.reference_values.items()]

    def reference_list(self):
        print(tabulate(self.table, headers=["Reference", "Potential (V)"]))

    def reference_difference(self):
        def interactive(old_reference="Ag/AgCl (sat. KCl)", new_reference="SHE", pH="1", potential="0"):
            if old_reference == "RHE" or new_reference == "RHE":
                self.reference_values["RHE"] = -0.0592 * float(pH)
            self.reference_difference_value = float(potential) + self.reference_values[new_reference] - self.reference_values[old_reference]
            return self.reference_difference_value
        widgets.interact(interactive, old_reference=list(self.reference_values.keys()), new_reference=list(self.reference_values.keys()))
        
        


class Chronopotentiometry:
    def __init__(self,e_chem,experiment_list,add_potential_value=None,new_reference_name=None,change_reference=False):
        self.reference = e_chem.experiments[experiment_list[0]].electrode_setup.reference_electrode
        self.e_chem = e_chem
        self.experiment_list=experiment_list
        self.df_liste=[]
        self.xlabel=f"$t$ ({e_chem.experiments[experiment_list[0]].analysis.cp.measurement_time_unit})"
        self.ylabel=f"$E$ vs. {self.reference} ({e_chem.experiments[experiment_list[0]].analysis.cp.measurement_potential_unit})"
        self.induced_current_density=e_chem.experiments[experiment_list[0]].analysis.cp.induced_current[0]/ e_chem.experiments[experiment_list[0]].electrode_setup.working_electrode_area
        mapping_dict={"cm^2":"cm$^2$",
                      "mm^2":"mm$^2$"}
        area_unit=mapping_dict[e_chem.experiments[experiment_list[0]].electrode_setup.working_electrode_area_unit]
        self.induced_current_density_unit=e_chem.experiments[experiment_list[0]].analysis.cp.induced_current_unit + "/"+ area_unit
        for experiment in range(0,len(e_chem.experiments)):
            if e_chem.experiments[experiment].type=="CP":
                df = pd.read_csv(e_chem.experiments[experiment].filename, sep="\t", header=56, skiprows=[57], usecols=[2,3,4,5],names=["t","E","I","V"])
                self.df_liste.append(df)
            else:
                self.df_liste.append(None)
        if change_reference:
            self.delta_E=add_potential_value
            self.reference=new_reference_name
            self.ylabel=f"$E$ vs. {self.reference} ({e_chem.experiments[experiment_list[0]].analysis.cp.measurement_potential_unit})"
            for df in self.df_liste:
                if df is not None:
                    df['E'] = df['E'] + self.delta_E
        else:
            pass
    def quick_plot(self):
        for experiment in self.experiment_list:
            f, (ax,ax2,ax3) = plt.subplots(3,1)
            f.suptitle(e_chem.experiments[experiment].name)
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
        if e_chem.experiments[self.experiment_list[0]].electrolyte.solvent=="H$_2$O":
            annotate_text=f"{e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration} {e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration_unit} {e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt} {e_chem.experiments[self.experiment_list[0]].electrolyte.solvent} pH={e_chem.experiments[self.experiment_list[0]].electrolyte.pH} \n$J$={self.induced_current_density} {self.induced_current_density_unit}"
        else:
            annotate_text=f"{e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration} {e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration_unit} {e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt} {e_chem.experiments[self.experiment_list[0]].electrolyte.solvent} \n$J$={self.induced_current_density} {self.induced_current_density_unit}"
        def interactive(xlabel=self.xlabel, ylabel=self.ylabel,savename="CP_plot.pdf",xcoord=(0,1.2,0.05),ycoord=(0,1.2,0.05),annotate_text=widgets.Textarea(value=annotate_text),save=False,annotate=True,legend=True):
            fig, ax = plt.subplots() 
            for experiment in self.experiment_list:
                ax.plot(self.df_liste[experiment]["t"], self.df_liste[experiment]["E"],label=e_chem.experiments[experiment].name)
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            if legend:
                ax.legend(loc="best",frameon=False)
            if annotate:
                ax.annotate(annotate_text,xy=(xcoord,ycoord),xycoords="axes fraction")
            if save:
                fig.savefig("plots/" + savename,bbox_inches='tight')
        widgets.interact(interactive)

    def end_value(self):
        def interactive(xlabel=self.xlabel, ylabel=self.ylabel,savename="CP_plot.pdf",last_points=75,save=False):
            names=[]
            end_values=[] 
            fig,ax =plt.subplots()
            for experiment in self.experiment_list:
                last_values = self.df_liste[experiment].tail(last_points)["E"].values[0]
                average = last_values.mean()
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
                ax.plot(self.df_liste[experiment]["t"], self.df_liste[experiment]["E"],label=e_chem.experiments[experiment].name)
                ax.plot(self.df_liste[experiment]["t"], [average] * len(self.df_liste[experiment]["t"]), linewidth=3,linestyle='dotted', label="{} average".format(e_chem.experiments[experiment].name))
                ax.legend(loc="best",frameon=False)
                names.append(e_chem.experiments[experiment].name)
                end_values.append(average) 
                if save:
                    fig.savefig("plots/" + savename,bbox_inches='tight') 
            self.end_value_df = pd.DataFrame(list(zip(names,end_values)), columns=["Name",f"Average of {last_points}"]) 
            return  self.end_value_df
        widgets.interact(interactive,last_points=(1,200))
    def end_value_fit(self):
        def exponential_fit(x, a, b, c):
            return a * np.exp(-b/2 * x) + c
        names=[]
        end_values=[]
        def interactive(xlabel=self.xlabel, ylabel=self.ylabel,savename="CA_plot.pdf",save=False):
            fig,ax =plt.subplots()
            for experiment in self.experiment_list:
                t_fit = np.linspace(0, self.df_liste[experiment]["t"].max(), self.df_liste[experiment].shape[0])
                popt, pcov = curve_fit(exponential_fit,self.df_liste[experiment]["t"], self.df_liste[experiment]["E"])
                c=popt[2]
                names.append(e_chem.experiments[experiment].name)
                end_values.append(c)
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
                ax.plot(self.df_liste[experiment]["t"], self.df_liste[experiment]["E"],label=e_chem.experiments[experiment].name)
                ax.plot(t_fit, exponential_fit(t_fit, *popt),linewidth=3,linestyle='dotted', label="{} fit".format(e_chem.experiments[experiment].name))
                ax.legend(loc="best",frameon=False)
                if save:
                    fig.savefig("plots/" + savename,bbox_inches='tight')
                self.end_value_fit_df = pd.DataFrame(list(zip(names,end_values)), columns=["Name","End value"])   
            return  self.end_value_fit_df
        widgets.interact(interactive)

class Chronoamperometry:
    def __init__(self,e_chem,experiment_list,current_density=False):
        self.induced_potential= e_chem.experiments[experiment_list[0]].analysis.ca.induced_potential[0]
        self.e_chem = e_chem
        self.experiment_list=experiment_list
        self.df_liste=[]
        mapping_dict_current = {"A": "A",
                                "mA": "mA",
                                "µA": "$\mathrm{\mu}$A",   
                                "nA": "nA"}
        current_label=mapping_dict_current[e_chem.experiments[experiment_list[0]].analysis.ca.measurement_current_unit]
        self.xlabel=f"$t$ ({e_chem.experiments[experiment_list[0]].analysis.ca.measurement_time_unit})"
        self.ylabel=f"$I$ ({current_label})" 
        mapping_dict={"cm^2":"cm$^2$",
                      "mm^2":"mm$^2$"}
        area_unit=mapping_dict[e_chem.experiments[experiment_list[0]].electrode_setup.working_electrode_area_unit]
        for experiment in range(0,len(e_chem.experiments)):
            if e_chem.experiments[experiment].type=="CA" and e_chem.experiments[experiment].filename.endswith(".dat"):
                df = pd.read_csv(e_chem.experiments[experiment].filename, sep="\s", header=0, names=["t", "I"],engine="python")
                self.df_liste.append(df)
            elif e_chem.experiments[experiment].type=="CA" and e_chem.experiments[experiment].filename.endswith(".txt"):
                df=pd.read_csv(e_chem.experiments[experiment].filename,header=0,sep=";",decimal=',',usecols=[0,2],names=["t","I"])
                self.df_liste.append(df)
            elif e_chem.experiments[experiment].type=="CA" and e_chem.experiments[experiment].filename.endswith(".csv"):
                df = pd.read_csv(e_chem.experiments[experiment].filename, sep=",", header=4, skipfooter=1, names=["t", "I"])
                self.df_liste.append(df)
            else:
                self.df_liste.append(None)
                pass 
        if current_density:
            self.ylabel=f"$J$ ({e_chem.experiments[experiment_list[0]].analysis.ca.measurement_current_unit}/{area_unit})"
            for df in self.df_liste:
                if df is not None:
                    for experiment in range(len(e_chem.experiments)):
                        df["I"] = df["I"] / e_chem.experiments[experiment].electrode_setup.working_electrode_area
    def plot(self):
        if e_chem.experiments[self.experiment_list[0]].electrolyte.solvent=="H$_2$O":
            annotate_text=f"{e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration} {e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration_unit} {e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt} {e_chem.experiments[self.experiment_list[0]].electrolyte.solvent} pH={e_chem.experiments[self.experiment_list[0]].electrolyte.pH} \n$E$={e_chem.experiments[self.experiment_list[0]].analysis.ca.induced_potential[0]} {e_chem.experiments[self.experiment_list[0]].analysis.ca.induced_potential_unit}"
        else:
            annotate_text=f"{e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration} {e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt_concentration_unit} {e_chem.experiments[self.experiment_list[0]].electrolyte.conducting_salt} {e_chem.experiments[self.experiment_list[0]].electrolyte.solvent}  \n$E$={e_chem.experiments[self.experiment_list[0]].analysis.ca.induced_potential[0]} {e_chem.experiments[self.experiment_list[0]].analysis.ca.induced_potential_unit}"
        def interactive(xlabel=self.xlabel, ylabel=self.ylabel,savename="CA_plot.pdf",xcoord=(0,1.2,0.05),ycoord=(0,1.2,0.05),annotate_text=widgets.Textarea(value=annotate_text),save=False,annotate=True,legend=True):
            fig, ax = plt.subplots() 
            for experiment in self.experiment_list:
                ax.plot(self.df_liste[experiment]["t"], self.df_liste[experiment]["I"], label=e_chem.experiments[experiment].name)

            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            if legend:
                ax.legend(loc="best",frameon=False)
            if save:
                fig.savefig("plots/" + savename,savename,bbox_inches='tight')
            if annotate:
                ax.annotate(annotate_text,xy=(xcoord,ycoord),xycoords="axes fraction")
        widgets.interact(interactive)
    def end_value_fit(self):
        def exponential_fit(x, a, b, c):
            return a * np.exp(-b/2 * x) + c
        names=[]
        end_values=[]
        #ylabel=r"$I$  ($\mathrm{\mu}$A)" use $\mathrm{\mu} if Latex rendering
        def interactive(xlabel=self.xlabel, ylabel=self.ylabel,savename="CA_plot.pdf",save=False):
            fig,ax =plt.subplots()
            for experiment in self.experiment_list:
                t_fit = np.linspace(0, self.df_liste[experiment]["t"].max(), self.df_liste[experiment].shape[0])
                popt, pcov = curve_fit(exponential_fit,self.df_liste[experiment]["t"], self.df_liste[experiment]["I"])
                c=popt[2]
                names.append(e_chem.experiments[experiment].name)
                end_values.append(c)
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
                ax.plot(self.df_liste[experiment]["t"], self.df_liste[experiment]["I"],label=e_chem.experiments[experiment].name)
                ax.plot(t_fit, exponential_fit(t_fit, *popt),linewidth=3,linestyle='dotted', label="{} fit".format(e_chem.experiments[experiment].name))
                ax.legend(loc="best",frameon=False)
                if save:
                    fig.savefig("plots/" + savename,bbox_inches='tight')
                self.end_value_fit_df = pd.DataFrame(list(zip(names,end_values)), columns=["Name","End value"])   
            return  self.end_value_fit_df
        widgets.interact(interactive)
    def end_value(self):

        def interactive(xlabel=self.xlabel, ylabel=self.ylabel,savename="CP_plot.pdf",last_points=75,save=False):
            names=[]
            end_values=[] 
            fig,ax =plt.subplots()
            for experiment in self.experiment_list:
                last_values = self.df_liste[experiment].tail(last_points)["I"].values[0]
                average = last_values.mean()
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
                ax.plot(self.df_liste[experiment]["t"], self.df_liste[experiment]["I"],label=e_chem.experiments[experiment].name)
                ax.plot(self.df_liste[experiment]["t"], [average] * len(self.df_liste[experiment]["t"]), linewidth=3,linestyle='dotted', label="{} average".format(e_chem.experiments[experiment].name))
                ax.legend(loc="best",frameon=False)
                names.append(e_chem.experiments[experiment].name)
                end_values.append(average) 
                if save:
                    fig.savefig("plots/" + savename,bbox_inches='tight') 
            self.end_value_df = pd.DataFrame(list(zip(names,end_values)), columns=["Name", f"Average of {last_points}"]) 
            return  self.end_value_df
        widgets.interact(interactive,last_points=(1,200))

