# Data model for Electrochemistry
 
## Objects

### Dataset
- __name__ 
  - Type: string
  - Description: Name of the dataset
- __date__
  - Type: date
  - Description: Date/time when the dataset was created
- __author__
  - Type: Author
  - Multiple: True
  - Description: Persons who worked on the dataset
- __sample__
  - Type: Sample
  - Multiple: True
  - Description: The sample which was measured 
- __analysis__
  - Type: Analysis
  - Description: The method which is used to gain the data
- __solvent__
  - Type: string
  - Description: Name of the solvent    
- __conducting_salt__
  - Type: string
  - Description: Name of the used salt
- __conducting_salt_concentration__
  - Type: Concentration_units
  - Description: Concentration of the conducting salt 
- __electrode_setup__
  - Type: Electrode_setup
  - Description: Name of the used electrode materials

### Sample
- __name_product__
  - Type: string
  - Description: The name of the product
- __chemical_formula__
  - Type: string  
  - Description: The chemical formula of the product
- __molecular_weight__
  - Type: Molecular_weight_units
  - Description: The molecular weight of the product 
- __synthesis__
  - Type: Synthesis
  - Description: The synthesis of the product 
- __film_preparation__
  - Type: Film_preparation
  - Description: The film preparation of the product
### Synthesis
- __reagents__
  - Type: string
  - Description: The reagents of the product
- __solvent__
  - Type: string
  - Description: The solvent of the synthesis
- __physical_parameters__
  - Type: Physical_parameters
  - Description: The physical parameters of the synthesis
### Physical_parameters
- __temperature__
  - Type: Temperature_units
  - Description: The used temperature for the synthesis 
- __pressure__
  - Type: Pressure_units
  - Description: The used pressure for the synthesis 
- __time__
  - Type: Time_units
  - Description: The used time for the synthesis  
### Film_preparation
- __spin_coating__
  - Type: Spin_coating
  - Multiple: True
  - Description: Spin coating parameter
### Spin_coating
- __volume__
  - Type: Volume_units
  - Description: The volume which was used for the film 
- __rotation__
  - Type: float
  - Multiple: True
  - Description: The rotation speed of the spin coating process
- __time__
  - Type: Time_units
  - Description: The rotation time 
- __annealing_temperature__
  - Type: Temperature_units
  - Description: The annealing temperature for the film
- __annealing_time__
  - Type: Time_units
  - Description: The annealing time for the film

  




### Analysis
- __cv__
  - Type: CV
  - Multiple: True
  - Description: Cyclic voltammetry
- __ca__
  - Type: CA
  - Multiple: True
  - Description: Chronoamperometry
- __cp__
  - Type: CP
  - Multiple: True
  - Description: Chronopotentiometry
### CP

- __induced_current_first__
  - Type: Current_units
  - Description: The first induced current  
- __induced_current_second__
  - Type: Current_units
  - Description: The first induced current  
- __time_duration__
  - Type: Time_units
  - Description: The duration time of the induced current
- __potential_end_value__
  - Type: Potential_units
  - Description: The potential value at the end of the measurement
- __charge_density__
  - Type: Charge_density_units
  - Multiple: True
  - Description: The charge density of the measurement 




### CA

- __induced_potential_first__
  - Type: Potential_units
  - Description: The first induced potential  
- __induced_potential_second__
  - Type: Potential_units
  - Description: The second induced potential
- __time_duration__
  - Type: Time_units
  - Description: The duration time of the induced potential
- __current_end_value__
  - Type: Current_units
  - Description: The current value at the end of the measurement 
### CV
Container for information regarding the CV-Setup and parameters
- __ferrocene_reference__
  - Type: Ferrocene_reference
  - Multiple: True
  - Description: Parameters of the ferocene reference measurement
- __halfe_wave_potential__
  - Type: Potential_units
  - Multiple: True
  - Description: The half-wave potential of the measurement  
- __scan_rate__
  - Type: Scan_rate_units
  - Description: The scan rate of the measurement 
- __start_potential__
  - Type: Potential_units
  - Description: The starting value of the potential 
- __stop_potential__
  - Type: Potential_units
  - Description: The stop value of the potential 
- __potential_lower_limit__
  - Type: Potential_units
  - Description: The lower limit of the potential
- __potential_upper_limit__
  - Type: Potential_units
  - Description: The upper limit of the potential
- __i_pc_ox__
  - Type: Current_units
  - Multiple: True
  - Description: The current at the maximum of the cathodic peak (oxidation)
- __i_pa_red__
  - Type: Current_units
  - Multiple: True 
  - Description: The current at the maximum of the anodic peak (reduction)
- __ox_potential_E_pc__
  - Type: Potential_units
  - Multiple: True
  - Description: Potential at the maximum of the cathodic peak (reduction)
- __red_potential_E_pa__
  - Type: Potential_units
  - Multiple: True
  - Description: The current at the maximum of the anodic peak (oxidation)
- __total_cycle_number__
  - Type: int
  - Description: The total cycle number
### Ferrocene_reference
- __ox_potential_E_pc_ferrocene__
  - Type: Potential_units
  - Description: Potential at the maximum of the cathodic peak (reduction) of the ferrocene reference
- __red_potential_E_pa_ferrocene__
  - Type: Potential_units
  - Description: The current at the maximum of the anodic peak (oxidation) of the ferrocene reference
- __halfe_wave_potential_ferrocene__
  - Type: Potential_units
  - Description: The half-wave potential of the ferrocene measurement 

### Electrode_setup
- __working_electrode__
  - Type: string
  - Description: Name of the used working electrode
- __counter_electrode__
  - Type: string
  - Description: Name of the used counter electrode  
- __Reference_electrode__
  - Type: string
  - Description: Name of the used reference electrode 

### Author
Container for information regarding persons who worked on a dataset.

- __name__
  - Type: string
  - Description: Full name of the author
- __affiliation__
  - Type: string
  - Description: Organization the author is affiliated with
- __email__
  - Type: string
  - Description: Contact e-mail address of the author
- __orcid__
  - Type: string
  - Description: The ORCID of the author


## Enumerations

### Charge_density_units
``` python
COULOMB_PER_CUBIC_METER = "C / m**3"
```

### Pressure_units
```python
PASCAL = "Pa "
BAR = "bar"
MILLI_BAR = "mbar"
```
### Molecular_weight_units
```python
GRAM_PER_MOLE = "g / mole "
GRAM_PER_MILLI_MOLE = "g / mmole"
```
### Temperature_units
```python
CELCIUS = "C"
KELVIN = "K"
```
### Volume_units
```python
MILLI_LITER = "ml"
MICRO_LITER = "ul" 
NANO_LITER = "nl"
```
### Time_units
```python
HOUR = "h"
MIN = "min"
SEC = "s" 
MILLI_SEC = "ms"
MICRO_SEC = "us"
```
### Concentration_units
```python
MOLAR = "mole / l"
MILLI_MOLAR = "mmole / l"
MICRO_MOLAR = "umole / l"
NANO_MOLAR = "nmole / l"
GRAM_LITER = "g / l"
MILLIGRAM_LITER = "mg / l"
MICROGRAM_LITER = "ug / l"
NANGRAM_LITER = "ng / l"
``` 
### Scan_rate_units
```python
VOLT_PER_SEC = "V / s"
MILLI_VOLT_PER_SEC = "mV / s"
MICRO_VOLT_PER_SEC = "uV / s"
``` 
### Current_units
```python
AMPERE = "A"
MILLI_AMPERE = "mA"
MICRO_AMPERE = "uA"
NANO_AMPERE = "nA"
``` 
### Potential_units
```python
VOLT = "V"
MILLI_VOLT = "mV"
MICRO_VOLT = "uV"
NANO_VOLT = "nV"
``` 
