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
- __electrode_material__
  - Type: string
  - Description: Name of the used electrode material
- __analysis__
  - Type: Analysis
  - Description: The method which is used to gain the data
  
### Sample
- __name__
  - Type: string
  - Description: The name of the product
- __chemical_formula__
  - Type: string  
  - Description: The chemical formula of the product
- __synthesis__
  - Type: string
  - Description: The synthesis of the product 

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
- __solvent__
  - Type: string
  - Description: Name of the solvent    
- __conducting_salt__
  - Type: string
  - Description: Name of the used salt
- __conducting_salt_concentration__
  - Type: Concentration_units
  - Description: Concentration of the conducting salt
- __induced_current_first__
  - Type: Current_units
  - Description: The first induced current  
- __induced_current_second__
  - Type: Current_units
  - Description: The first induced current  
- __time_duration__
  - Type: Time_units
  - Description: The duration time of the induced current

### CA
- __solvent__
  - Type: string
  - Description: Name of the solvent    
- __conducting_salt__
  - Type: string
  - Description: Name of the used salt
- __conducting_salt_concentration__
  - Type: Concentration_units
  - Description: Concentration of the conducting salt
- __induced_potential_first__
  - Type: Potential_units
  - Description: The first induced potential  
- __induced_potential_second__
  - Type: Potential_units
  - Description: The second induced potential
- __time_duration__
  - Type: Time_units
  - Description: The duration time of the induced potential 
### CV
Container for information regarding the CV-Setup and parameters
- __solvent__
  - Type: string
  - Description: Name of the solvent    
- __conducting_salt__
  - Type: string
  - Description: Name of the used salt
- __conducting_salt_concentration__
  - Type: Concentration_units
  - Description: Concentration of the conducting salt 
- __halfe_wave_potential__
  - Type: Potential_units
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
  - Description: The current at the maximum of the cathodic peak (oxidation)
- __i_pa_red__
  - Type: Current_units
  - Description: The current at the maximum of the anodic peak (reduction)
- __ox_potential_E_pc__
  - Type: Potential_units
  - Description: Potential at the maximum of the cathodic peak (reduction)
- __red_potential_E_pa__
  - Type: Potential_units
  - Description: The current at the maximum of the anodic peak (oxidation)
- __total_cycle_number__
  - Type: int
  - Description: The total cycle number
### Author
Container for information regarding persons who worked on a dataset.

- __name__
  - Type: string
  - Description: Full name of the author
- __affiliation__
  - Type: string
  - Description: Organization the author is affiliated with
- email
  - Type: string
  - Description: Contact e-mail address of the author


## Enumerations

### Time_units
```python
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
MILLI_VOLT_SEC = "mV / s"
MICRO_VOLT_SEC = "uV / s"
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
