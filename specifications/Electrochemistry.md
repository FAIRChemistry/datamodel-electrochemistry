# Data model for Electrochemistry

## Objects

### Dataset

- name
  - Type: string
  - Description: Name of the dataset
- date_created
  - Type: date
  - Description: Date/time when the dataset was created
- author
  - Type: Author
  - Multiple: True
  - Description: Persons who worked on the dataset
- sample
  - Type: Sample
  - Multiple: True
  - Description: The sample which was measured
- analysis
  - Type: Analysis
  - Description: The method which is used to gain the data
- solvent
  - Type: string
  - Description: Name of the solvent
- conducting_salt
  - Type: string
  - Description: Name of the used salt
- conducting_salt_concentration
  - Type: enum
  - Description: Concentration of the conducting salt
- electrode_setup
  - Type: ElectrodeSetup
  - Description: Name of the used electrode materials
- experiment
  - Type: string
  - Multiple: True
  - Description: Name of the experiment files



### Sample

- name_product
  - Type: string
  - Description: The name of the product
- chemical_formula
  - Type: string  
  - Description: The chemical formula of the product
- molecular_weight
  - Type: MolecularWeightUnits
  - Description: The molecular weight of the product
- synthesis
  - Type: Synthesis
  - Description: The synthesis of the product
- film_preparation
  - Type: FilmPreparation
  - Description: The film preparation of the product

### Synthesis

- reagents
  - Type: string
  - Description: The reagents of the product
- solvent
  - Type: string
  - Description: The solvent of the synthesis
- physical_parameters
  - Type: PhysicalParameters
  - Description: The physical parameters of the synthesis

### PhysicalParameters

- temperature
  - Type: TemperatureUnits
  - Description: The used temperature for the synthesis
- pressure
  - Type: PressureUnits
  - Description: The used pressure for the synthesis
- time
  - Type: TimeUnits
  - Description: The used time for the synthesis  

### FilmPreparation

- spin_coating
  - Type: SpinCoating
  - Multiple: True
  - Description: Spin coating parameter

### SpinCoating

- volume
  - Type: VolumeUnits
  - Description: The volume which was used for the film
- rotation
  - Type: float
  - Multiple: True
  - Description: The rotation speed of the spin coating process
- time
  - Type: TimeUnits
  - Description: The rotation time
- annealing_temperature
  - Type: TemperatureUnits
  - Description: The annealing temperature for the film
- annealing_time
  - Type: TimeUnits
  - Description: The annealing time for the film

### Analysis

- cv
  - Type: CV
  - Multiple: True
  - Description: Cyclic voltammetry
- ca
  - Type: CA
  - Multiple: True
  - Description: Chronoamperometry
- cp
  - Type: CP
  - Multiple: True
  - Description: Chronopotentiometry
### DatasetForPlots
- filename
  - Type: string
  - Description: The filename with path
- reference
  - Type: string
  - Description: The reference
- name
  - Type: string
  - Description: The name
- conducting_salt
  - Type: string
  - Description: The conducting_salt
- concentration
  - Type: string
  - Description: The conducted_salt_concentration
- solvent
  - Type: string
  - Description: The solvent
- pH
  - Type: string
  - Description: The pH value
- scan_rate
  - Type: string
  - Description: The scan rate
- substrate
  - Type: string
  - Description: name of the substrate (WE)

### CP

- induced_current_first
  - Type: CurrentUnits
  - Description: The first induced current  
- induced_current_second
  - Type: CurrentUnits
  - Description: The first induced current  
- time_duration
  - Type: TimeUnits
  - Description: The duration time of the induced current
- potential_end_value
  - Type: PotentialUnits
  - Description: The potential value at the end of the measurement
- charge_density
  - Type: ChargeDensityUnits
  - Multiple: True
  - Description: The charge density of the measurement

### CA

- induced_potential_first
  - Type: PotentialUnits
  - Description: The first induced potential  
- induced_potential_second
  - Type: PotentialUnits
  - Description: The second induced potential
- time_duration
  - Type: TimeUnits
  - Description: The duration time of the induced potential
- current_end_value
  - Type: CurrentUnits
  - Description: The current value at the end of the measurement

### CV

Container for information regarding the CV-Setup and parameters

- ferrocene_reference
  - Type: Ferrocene_reference
  - Multiple: True
  - Description: Parameters of the ferocene reference measurement
- halfe_wave_potential
  - Type: PotentialUnits
  - Multiple: True
  - Description: The half-wave potential of the measurement  
- scan_rate
  - Type: ScanRateUnits
  - Description: The scan rate of the measurement
- start_potential
  - Type: PotentialUnits
  - Description: The starting value of the potential
- stop_potential
  - Type: PotentialUnits
  - Description: The stop value of the potential
- potential_lower_limit
  - Type: PotentialUnits
  - Description: The lower limit of the potential
- potential_upper_limit
  - Type: PotentialUnits
  - Description: The upper limit of the potential
- i_pc_ox
  - Type: CurrentUnits
  - Multiple: True
  - Description: The current at the maximum of the cathodic peak (oxidation)
- i_pa_red
  - Type: CurrentUnits
  - Multiple: True
  - Description: The current at the maximum of the anodic peak (reduction)
- ox_potential_E_pc
  - Type: PotentialUnits
  - Multiple: True
  - Description: Potential at the maximum of the cathodic peak (reduction)
- red_potential_E_pa
  - Type: PotentialUnits
  - Multiple: True
  - Description: The current at the maximum of the anodic peak (oxidation)
- total_cycle_number
  - Type: int
  - Description: The total cycle number

### Ferrocene_reference

- ox_potential_E_pc_ferrocene
  - Type: PotentialUnits
  - Description: Potential at the maximum of the cathodic peak (reduction) of the ferrocene reference
- red_potential_E_pa_ferrocene
  - Type: PotentialUnits
  - Description: The current at the maximum of the anodic peak (oxidation) of the ferrocene reference
- halfe_wave_potential_ferrocene
  - Type: PotentialUnits
  - Description: The half-wave potential of the ferrocene measurement

### ElectrodeSetup

- WE
  - Type: string
  - Description: Name of the used working electrode
- CE
  - Type: string
  - Description: Name of the used counter electrode  
- RE
  - Type: string
  - Description: Name of the used reference electrode

### Author

Container for information regarding persons who worked on a dataset.

- name
  - Type: string
  - Description: Full name of the author
- affiliation
  - Type: string
  - Description: Organization the author is affiliated with
- email
  - Type: string
  - Description: Contact e-mail address of the author
- orcid
  - Type: string
  - Description: The ORCID of the author

## Enumerations

### ChargeDensityUnits

``` python
COULOMB_PER_CUBIC_METER = "C / m**3"
```

### PressureUnits

```python
PASCAL = "Pa "
BAR = "bar"
MILLI_BAR = "mbar"
```

### MolecularWeightUnits

```python
GRAM_PER_MOLE = "g / mole "
GRAM_PER_MILLI_MOLE = "g / mmole"
```

### TemperatureUnits

```python
CELCIUS = "C"
KELVIN = "K"
```

### VolumeUnits

```python
MILLI_LITER = "ml"
MICRO_LITER = "ul" 
NANO_LITER = "nl"
```

### TimeUnits

```python
HOUR = "h"
MIN = "min"
SEC = "s" 
MILLI_SEC = "ms"
MICRO_SEC = "us"
```

### ConcentrationUnits

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

### ScanRateUnits

```python
VOLT_PER_SEC = "V / s"
MILLI_VOLT_PER_SEC = "mV / s"
MICRO_VOLT_PER_SEC = "uV / s"
```

### CurrentUnits

```python
AMPERE = "A"
MILLI_AMPERE = "mA"
MICRO_AMPERE = "uA"
NANO_AMPERE = "nA"
```

### PotentialUnits

```python
VOLT = "V"
MILLI_VOLT = "mV"
MICRO_VOLT = "uV"
NANO_VOLT = "nV"
```
