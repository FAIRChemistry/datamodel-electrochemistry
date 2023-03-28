# Datamodel for Electrochemistry
 
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
  - Description: cv
- __cp__
  - Type: CP
  - Multiple: True
  - Description: cp
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
  - Type: float
  - Description: The half-wave potential of the measurement in V 
- __scan_rate__
  - Type: Scan_rate_units
  - Description: The scan rate of the measurement 
- __start_potential__
  - Type: float
  - Description: The starting value of the potential in V 
- __stop_potential__
  - Type: float
  - Description: The stop value of the potential in V 
- __i_pc__
  - Type: Current_units
  - Description: The current at the maximum of the cathodic peak in A
- __i_pa__
  - Type: Current_units
  - Description: The current at the maximum of the anodic peak in A 
- __potential_E_pc__
  - Type: float
  - Description: Potential at the maximum of the cathodic peak in V
- __potential_E_pa__
  - Type: float
  - Description: The current at the maximum of the anodic peak in V
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
  - Description: Organisation the author is affiliated with
- __email__
  - Type: string
  - Description: Contact e-mail address of the author




  


#### Concentration_units
```python
MOLAR = "mole / l"
MILLI_MOLAR = "mmole / _l"
MICRO_MOLAR = "umole / l"
NANO_MOLAR = "nmole / l"
GRAM_LITER = "g / l"
MILLIGRAM_LITER = "mg / l"
MICROGRAM_LITER = "ug / l"
NANGRAM_LITER = "ng / l"
``` 
#### Scan_rate_units
```python
VOLT_SEC = "V / s"
MILLI_VOLT_SEC = "mV / s"
MICRO_VOLT_SEC = "uV / s"
``` 
#### Current_units
```python
AMPERE = "A"
MILLI_AMPERE = "mA"
MICRO_AMPERE = "uA"
NANO_AMPERE = "nA"
``` 