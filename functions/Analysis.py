import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 
import datetime
from scipy.optimize import curve_fit
from sdRDM import DataModel
from tabulate import tabulate
from scipy.integrate import trapz
class Analysis:
    def __init__(self):
        self.Ref_values={"SHE":0, 
              "RHE":-0.059, 
              "Calomel (sat. KCl)":0.241,
              "Calomel (3.5 M KCl)":0.250,
              "Calomel (1 M KCl)":0.280,
              "Calomel (0.1 M KCl)":0.334,
              "Ag/AgCl (sat. KCl)":0.199,
              "Ag/AgCl (3.5 M KCl)":0.205,
              "Hg/HgO (1 M KOH)":0.140,
              "Hg/HgO (0.1 M KOH)":0.165,
              "Fc/Fc+":0.400
              }  
        self.table = [[x, y] for x, y in self.Ref_values.items()]
        #print(tabulate(table, headers=["Reference", "Potential (V)"]))
    def reference_list(self):
        print(tabulate(self.table, headers=["Reference", "Potential (V)"]))
    def reference_difference(self,x,y):
       
        if x in self.Ref_values and y in self.Ref_values:
            if x=="RHE" or y== "RHE":
                pH= input("enter pH value:")
                self.Ref_values["RHE"]= -0.0592 * float(pH)
                #print(Ref_values["RHE"])
                return  self.Ref_values[x] - self.Ref_values[y]
            else:
                return  self.Ref_values[x] - self.Ref_values[y]
        else: 
            return None
class ChronoPotentiometry(Analysis):
    def __init__(self,metadata,change_referene=False):
        self.df = pd.read_csv(metadata.filename, sep="\t", header=56, skiprows=[57], usecols=[2, 3], names=["t", "E"])
        self.name=metadata.name if metadata.name is not None else ""
        self.solvent = metadata.solvent if metadata.solvent is not None else "H$_2$O"
        self.concentration = metadata.concentration if metadata.concentration is not None else "0.1 M"
        self.conducting_salt= metadata.conducting_salt if metadata.conducting_salt is not None else " KOH"
        self.pH= metadata.pH if metadata.pH is not None else ""
        self.reference = metadata.reference if metadata.reference is not None else "Hg/HgO"
        self.df_all=pd.read_csv(metadata.filename,sep="\t",header=56,skiprows=[57],usecols=[2,3,4,5],names=["t","E","I","V"])
        if change_referene:
            delta_E=float(input("Enter the reference differnce: "))
            self.df["E"] = self.df["E"] + delta_E
            self.reference= input("Enter the reference name: ")
        else:
            self.df["E"] = self.df["E"]
            self.reference= self.reference

    def quick_plot(self):
        f, (ax,ax2,ax3) = plt.subplots(3,1)
        f.suptitle("Raw data")
        ax.plot(self.df_all["t"], self.df_all["E"])
        ax2.plot(self.df_all["t"], self.df_all["I"])
        ax3.plot(self.df_all["t"], self.df_all["V"])
        ax.set_ylabel("$E$ vs Ref (V)")
        ax2.set_ylabel("$I$ (A)")
        ax3.set_ylabel("$V$ (V)")
        ax3.set_xlabel("$t$ (s)")
        ax.get_xaxis().set_visible(False)
        ax2.get_xaxis().set_visible(False)

    def plot(self, save=False,label=False): 
        xlabel="$t$ (s)"
        ylabel=f"$E$ vs. {self.reference} (V)"
        if label:
            xlabel= input("enter new xlabel: ")
            ylabel= input("enter new ylabel: ")
        fig,ax =plt.subplots()     
        ax.plot(self.df["t"],self.df["E"],label="{}/{} {} {}/{} ".format(self.name,self.concentration,self.conducting_salt,self.solvent,self.pH))
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.legend(loc="best",frameon=False,handlelength=0)
        plt.show()
        if save:
            plotname=input("Enter the name of the plot: ")
            fig.savefig(plotname,bbox_inches='tight')  

    def end_value_fit(self,save=False):
        def exponential_fit(x, a, b, c):
            return a * np.exp(-b * x) + c
        np.seterr(over='ignore')
        t_fit = np.linspace(0, self.df.shape[0], self.df.shape[0])
        fig,ax =plt.subplots()     
        popt, pcov = curve_fit(exponential_fit,self.df["t"].values, self.df["E"].values)
        c=popt[2]
        ax.plot(self.df["t"],self.df["E"],label=self.name)
        ax.plot(t_fit, exponential_fit(t_fit, *popt), 'r-', label="Fit")
        ax.legend(loc="best",frameon=False)
        plt.show()
        if save:
            plotname=input("Enter the name of the plot: ")
            fig.savefig(plotname,bbox_inches='tight')  
        return c
    
    def end_value(self,save=False):
        last_values = self.df.tail(20)["E"].values[0]
        average = last_values.mean()
        fig,ax =plt.subplots()   
        ax.plot(self.df["t"],self.df["E"],label=self.name)
        ax.plot(self.df["t"], [average] * len(self.df["t"]), 'r-', label="Average Line")
        ax.legend(loc="best",frameon=False)
        plt.show()
        if save:
            plotname=input("Enter the name of the plot: ")
            fig.savefig(plotname,bbox_inches='tight')  
        return average 
    
class MultiChronoPotentiometry(Analysis):
    def __init__(self, metadata_list,change_reference=False):
        self.reference = metadata_list[0].reference
        self.metadata_list = metadata_list
        if change_reference:
            self.delta_E=float(input("Enter the reference differnce: "))
            self.reference= input("Enter the reference name: ")
        else:
            self.delta_E=0
    def plot(self,save=False,label=False):
        xlabel="$t$ (s)"
        ylabel=f"$E$ vs. {self.reference} (V)"
        if label:
            xlabel= input("enter new xlabel: ")
            ylabel= input("enter new ylabel: ")
        fig, ax = plt.subplots()
        for metadata in self.metadata_list:
            df = pd.read_csv(metadata.filename, sep="\t", header=56, skiprows=57, usecols=[2, 3], names=["t", "E"])
            ax.plot(df["t"], df["E"]+self.delta_E,label=metadata.name)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.legend(loc="best",frameon=False)
        #ax.annotate((metadata["solvent"],metadata["scan_rate"]),xy=(0.6,0.1),xycoords="axes fraction")
        plt.show()
        if save:
            plotname=input("Enter the name of the plot: ")
            fig.savefig(plotname,bbox_inches='tight') 
class ChronoAmperometry(Analysis):
     def __init__(self, metadata,current_density=False):
         if metadata.filename.endswith(".csv"):
            self.df = pd.read_csv(metadata.filename, sep=",", header=4, skipfooter=1, names=["t", "I"],engine="python")
         elif metadata.filename.endswith(".dat"):
             self.df = pd.read_csv(metadata.filename, sep="\s", header=0, names=["t", "I"],engine="python")
         self.name= metadata.name if metadata.name is not None else "" 
         self.solvent = metadata.solvent if metadata.solvent is not None else "H$_2$O"
         self.concentration = metadata.concentration if metadata.concentration is not None else "0.1 M"
         self.conducting_salt= metadata.conducting_salt if metadata.conducting_salt is not None else " KOH"
         self.reference = metadata.reference if metadata.reference is not None else "Hg/HgO"
         self.xlabel="$t$ (s)"
         self.ylabel="$I$ (A)"
         if current_density:
             self.A=float(input("Enter the WE area:"))
             self.df["I"]=self.df["I"]/self.A
             J_unit= input("Enter the unit of your current density (Use $ symbols for exponent eg. A/cm$^2$ ): ")
             self.ylabel= f"$J$  ({J_unit})"   

     def plot(self,save=False,label=False):
         xlabel=self.xlabel 
         ylabel=self.ylabel
         if label:
            xlabel= input("enter new xlabel: ")
            ylabel= input("enter new ylabel: ")
         fig, ax = plt.subplots()
         ax.plot(self.df["t"],self.df["I"],label="{} / {} {} ".format(self.name,self.concentration,self.conducting_salt))
         ax.set_xlabel(xlabel)
         ax.set_ylabel(ylabel)
         ax.legend(loc="best", frameon=False, handlelength=0)
         plt.show()
         if save:
            plotname=input("Enter the name of the plot: ")
            fig.savefig(plotname,bbox_inches='tight')

     def end_value_fit(self,save=False):
         def exponential_fit(x, a, b, c):
            return a * np.exp(-b * x) + c
         popt, pcov = curve_fit(exponential_fit,self.df["t"].values, self.df["I"].values)
         np.seterr(over='ignore')
         t_fit = np.linspace(0, self.df.shape[0], self.df.shape[0])
         fig,ax =plt.subplots()     
         popt, pcov = curve_fit(exponential_fit,self.df["t"].values, self.df["I"].values)
         c=popt[2]
         ax.plot(self.df["t"],self.df["I"],label=self.name)
         ax.plot(t_fit, exponential_fit(t_fit, *popt), 'r-', label="Fit")
         ax.legend(loc="best",frameon=False)
         plt.show()
         if save:
            plotname=input("Enter the name of the plot: ")
            fig.savefig(plotname,bbox_inches='tight')  
         return c
     
     def end_value(self,save=False):
         last_values = self.df.tail(20)["I"].values[0]
         average =last_values.mean()
         fig,ax =plt.subplots()   
         ax.plot(self.df["t"],self.df["I"],label=self.name)
         ax.plot(self.df["t"], [average] * len(self.df["t"]), 'r-', label="Average Line")
         ax.legend(loc="best",frameon=False)
         plt.show()
         if save:
            plotname=input("Enter the name of the plot: ")
            fig.savefig(plotname,bbox_inches='tight')  
         return average

class MultiChronoAmperometry(Analysis):
    def __init__(self, metadata_list,current_density=False):
        self.reference = metadata_list[0].reference
        self.metadata_list = metadata_list
        self.xlabel="$t$ (s)"
        self.ylabel="$I$ (A)"
        if current_density:
            self.A=float(input("Enter the WE area:"))
            J_unit= input("Enter the unit of your current density (Use $ symbols for exponent eg. A/cm$^2$ ): ")
            self.ylabel= f"$J$  ({J_unit})"
        else:
            self.A=1
        print( self.metadata_list)
    def plot(self,save=False,label=False):
        xlabel=self.xlabel
        ylabel=self.ylabel
        if label:
            xlabel= input("enter new xlabel: ")
            ylabel= input("enter new ylabel: ")
        fig, ax = plt.subplots()
        for metadata in self.metadata_list:
            if metadata.filename.endswith(".csv"):
                df = pd.read_csv(metadata.filename, sep=",", header=4, skipfooter=1, names=["t", "I"],engine="python")
            elif metadata.filename.endswith(".dat"):
                df = pd.read_csv(metadata.filename, sep="\s", header=0, names=["t", "I"],engine="python")
            ax.plot(df["t"], df["I"]/self.A,label=metadata.name)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.legend(loc="best",frameon=False)
        plt.show()
        if save:
            plotname=input("Enter the name of the plot:")
            fig.savefig(plotname,bbox_inches='tight') 
class CyclicVoltammetry(Analysis):
    def __init__(self,metadata,cycles=None,current_density=False,change_reference=False):
        self.df = pd.read_csv(metadata.filename,header=5,skipfooter=1,engine="python")
        self.total_cycles=len(self.df. columns) // 2
        self.all_cycles_list= [i for i in range(1,self.total_cycles+1)]
        self.solvent = metadata.solvent if metadata.solvent is not None else "MeCN"
        self.cycles= cycles if cycles is not None else self.all_cycles_list
        self.concentration = metadata.concentration if  metadata.concentration is not None else "0.1 M"
        self.conducting_salt =  metadata.conducting_salt if metadata.conducting_salt is not None else " KOH"
        self.substrate= metadata.substrate if metadata.substrate is not None else "Au"
        self.scan_rate= metadata.scan_rate if metadata.scan_rate is not None else "20 mV/s"
        self.reference = metadata.reference if metadata.reference is not None else "Ag/AgCl"
        self.name= metadata.name if metadata.name is not None else "" 
        self.E = ["E" for i in range(self.total_cycles)]
        self.I = ["I" for i in range(self.total_cycles)]
        self.df.columns = [name for pair in zip(self.E, self.I) for name in pair]
        self.num_cycles = int(self.df.shape[1] / 2)
        self.cycle_df = np.array_split(self.df, self.num_cycles, axis=1)
        self.cycles = [cycle-1 for cycle in self.cycles]
        if change_reference:
            delta_E=float(input("Enter the reference differnce: "))
            self.reference= input("Enter the reference name: ")
            for df in self.cycle_df:
                df['E'] = df['E'] + delta_E
        self.xlabel= f"$E$ vs. {self.reference}  (V)"
        self.ylabel= r"$I$  ($\mathrm{\mu}$A)" ### \textmu if latex rendering
        if current_density:
            A=float(input("Enter the WE area:"))
            J_unit= input("Enter the unit of your current density (Use $ symbols for exponent eg. A/cm$^2$ ): ")
            self.df["I"] = self.df["I"] / A
            self.ylabel= f"$J$  ({J_unit}) "
            for df in self.cycle_df:
                df['I'] = df['I'] / A
        #pass
    def plot(self,xy=None,save=False,label=False):
        xy= xy if xy is not None else (0.75,.02)
        fig, ax=plt.subplots()
        xlabel=self.xlabel
        ylabel=self.ylabel
        if label:
            xlabel= input("enter new xlabel: ")
            ylabel= input(r"enter new ylabel: ")
        ax.annotate(f"{self.concentration} {self.conducting_salt}/{self.substrate}\n$v$ = {self.scan_rate}", xy=xy, xycoords="axes fraction")
        for i in self.cycles: 
            ax.plot(self.cycle_df[i]["E"],self.cycle_df[i]["I"],label="Cycle: {}".format(i+1))
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.legend(loc="best",frameon=False)
        plt.show()

        if save:
            plotname=input("Enter the name of the plot: ")
            fig.savefig(plotname,bbox_inches='tight')
    def peaks(self,range=None):
        E_min=[]
        E_max=[]
        E_hwp=[]
        Cycles=[]
        I_max=[]
        I_min=[]
        I_vertex_list=[]
        x_max = self.cycle_df[0]['E'].max()
        x_min = self.cycle_df[0]['E'].min()
        range= range if range is not None else (x_min,x_max) 
        for i in self.cycles:
            Cycles.append("Cycle: {}".format(i+1))
            indices = np.where((self.cycle_df[i]["E"] >= range[0]) & (self.cycle_df[i]["E"] <= range[1]))[0]
            max_index = indices[np.argmax(self.cycle_df[i]["I"][indices])]
            pot_at_max = self.cycle_df[i]["E"][max_index]
            current_at_max = self.cycle_df[i]["I"][max_index]
            min_index = indices[np.argmin(self.cycle_df[i]["I"][indices])]
            pot_at_min = self.cycle_df[i]["E"][min_index]
            current_at_min = self.cycle_df[i]["I"][min_index]
            max_E= np.argmax(self.cycle_df[i]["E"])
            min_E= np.argmin(self.cycle_df[i]["E"])
            I_at_max_E=self.cycle_df[i]["I"][max_E]
            I_at_min_E=self.cycle_df[i]["I"][min_E]
            I_start=self.cycle_df[i]["I"][0]
            if self.cycle_df[0]["E"][0]< self.cycle_df[0]["E"][10]:
                I_vertex=I_at_max_E-I_start
            else:
                I_vertex=I_at_min_E-I_start
            E_max.append(pot_at_max)
            E_min.append(pot_at_min)
            E_hwp.append((pot_at_max+pot_at_min)/2 )
            I_min.append(current_at_min)
            I_max.append(current_at_max)
            I_vertex_list.append(I_vertex)
            df = pd.DataFrame(list(zip(Cycles,E_min,E_max,I_min,I_max,E_hwp,I_vertex_list)), columns=["Cycles",'E min','E max',"I min","I max","E1/2","I_vertex"])   
        return  df   
    def integration(self,range=None):
        Cycles=[]
        Integral=[]
        x_max = self.cycle_df[0]['E'].max()
        x_min = self.cycle_df[0]['E'].min()
        range= range if range is not None else (x_min,x_max)
        for i in self.cycles:
            Cycles.append("Cycle: {}".format(i+1)) 
            df=self.cycle_df[i]
            half= len(df)//2
            df1=df.iloc[:half,:]
            df2=df.iloc[half:,:]
            #plt.plot(df1["E"],df1["I"])
            #plt.plot(df2["E"],df2["I"])
            indices = np.where((df1["E"] >= range[0]) & (df1["E"] <= range[1]))[0]
            indices2 = np.where((df2["E"] >= range[0]) & (df2["E"] <= range[1]))[0]
            # area cant be with indices2 I dont know why
            area1 = trapz(df1['I'][indices],df1['E'][indices])
            area2 = trapz(df2['I'],df2['E'])   
            Integral.append((area1,area2))
            dataframe = pd.DataFrame(zip(Cycles,Integral), columns=["Cycles","Integration Area"])
        return dataframe
