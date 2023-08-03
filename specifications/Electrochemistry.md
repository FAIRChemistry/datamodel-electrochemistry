# Data model for Electrochemistry

## Objects

### Dataset

- general_information
  - Type: GeneralInformation
  - Description: General information about the data model
- experiments
  - Type: Experiment
  - Multiple: True
  - Description: The experiments for work


### GeneralInformation
- title
  - Type: string
  - Description: The title of the work
- author
  - Type: Author
  - Multiple: True
  - Description: Persons who worked on the dataset  
- date_of_work
  - Type: date
  - Description: Date/time when the dataset was created
  
### Experiment
- name
  - Type: string
  - Description: Name of the experiment
- filename
  - Type: string
  - Description: Name of the experiment file (with the path)
- information
  - Type: string
  - Description: Information of the experiment
- electrode_setup
  - Type: ElectrodeSetup
  - Description: Name of the used electrode materials
- electrolyte
  - Type: Electrolyte
  - Description: The used electrolyte
- analysis
  - Type: Analysis
  - Description: The analysis type of the experiment
- type
  - Type: Experiment_type
  - Description: Type of experiment



### Electrolyte
- solvent
  - Type: string
  - Description: Name of the solvent
- conducting_salt
  - Type: string
  - Description: Name of the used salt
- conducting_salt_concentration
  - Type: float
  - Description: Concentration of the conducting salt
- conducting_salt_concentration_unit
  - Type: ConcentrationUnits
  - Description: Unit of the conducting salt concentration
- pH
  - Type: float
  - Description: The pH value

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
- cp
  - Type: CP
  - Description: Chronopotentiometry
- ca
  - Type: CA
  - Description: Chronoamperometry
- cv
  - Type: CV
  - Description: Cyclic Voltammetry
  
### CP
- measurement_potential_unit
  - Type: PotentialUnits
  - Description: The potential unit of the measurement 
- measurement_time_unit
  - Type: TimeUnits
  - Description: The time unit of the measurement
- induced_current
  - Type: float
  - Multiple: True
  - Description: The induced current  
- induced_current_unit
  - Type: CurrentUnits
  - Description: The induced current unit
- time_duration
  - Type: float
  - Description: The duration time of the induced current
- time_duration_unit
  - Type: TimeUnits
  - Description: The duration time unit of the induced current
- potential_end_value
  - Type: PotentialEndValue
  - Multiple: True
  - Description: The potential value at the end of the measurement
- charge_density
  - Type: ChargeDensityUnits
  - Multiple: True
  - Description: The charge density of the measurement
- change_potential
  - Type: float
  - Multiple: True
  - Description: A list of potential values, which could be used to transform reference potential scale 

### PotentialEndValue
- method
  - Type: string
  - Description: The method, which was used to determine this value
- end_value
  - Type: float
  - Description: The end value potential
- reference_name
  - Type: string
  - Description: The used reference scale
- change_reference_potential
  - Type: float
  - Description: The change_reference potential
- last_average_points
  - Type: int
  - Description: The last points, which were used to calculate the average
- fit_function
  - Type: string
  - Description: The fit function, if the fit function was used 


### CA
- measurement_current_unit
  - Type: CurrentUnits
  - Description: The current unit of the measurement 
- measurement_time_unit
  - Type: TimeUnits
  - Description: The time unit of the measurement
- induced_potential
  - Type: float
  - Multiple: True
  - Description: The induced current  
- induced_potential_unit
  - Type: PotentialUnits
  - Description: The induced current unit
- time_duration
  - Type: float
  - Description: The duration time of the induced current
- time_duration_unit
  - Type: TimeUnits
  - Description: The duration time unit of the induced current
- current_end_value
  - Type: CurrentUnits
  - Description: The current value at the end of the measurement

### CV

Container for information regarding the CV-Setup and parameters
- changing_potential
  - Type: float
  - Multiple: True
  - Description: The potential which should be added 
- changing_potential_unit
  - Type: float
  - Description: The unit of the added potential 
- ferrocene_potential
  - Type: float
  - Description: ferrocene_potential
- measurement_current_unit
  - Type: CurrentUnits
  - Description: The current unit of the measurement 
- measurement_potential_unit
  - Type: PotentialUnits
  - Description: The unit of the Potential
- scan_rate
  - Type: float
  - Description: The scan rate of the measurement
- scan_rate_unit
  - Type: ScanRateUnits
  - Description: The scan rate unit of the measurement
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
- change_potential
  - Type: float
  - Multiple: True
  - Description: A tuple list of potential values, which could be used to transform reference potential scale 
- cycles
  - Type: Cycle
  - Multiple: True
  - Description: The cycles

### Cycle
- number
  - Type: int
  - Description: The cycle number
- peaks_and_half_potential
  - Type:PeaksAndHalfPotential
  - Multiple: True
  - Description: The half-wave potential of the measurement
- peak_integration
  - Type: PeakIntegration
  - Multiple: True
  - Description: The peak integration
### PeaksAndHalfPotential
- current_maximum
  - Type: float
  - Description: A list of the peak maxima
- current_minimum
  - Type: float
  - Description: A list of the peak minima
- potential_maximum
  - Type: float
  - Description: A list of the peak maxima
- potential_minimum
  - Type: float
  - Description: A list of the peak minima
- y_unit
  - Type: string
  - Description: The y unit 
- change_reference_potential
  - Type: float
  - Description: The change_reference potential
- reference_name
  - Type: string
  - Description: The used reference scale
- half_wave_potential
  - Type: float
  - Description: The half-wave potential of the measurement
### PeakIntegration
- lower_limit_potential
  - Type: float
  - Description: Name of the used working electrode 
- upper_limit_potential
  - Type: float
  - Description: Name of the used working electrode 
- integration_area
  - Type: float
  - Description: Name of the used working electrode
- integration_area_unit
  - Type: string
  - Description: Name of the used working electrode
- integration_direction
  - Type: string
  - Description: The integration direction.

### ElectrodeSetup

- working_electrode
  - Type: string
  - Description: Name of the used working electrode 
- working_electrode_area
  - Type: float
  - Description: The area of the used working electrode
- working_electrode_area_unit
  - Type: AreaUnits
  - Description: The area of the used working electrode
- counter_electrode
  - Type: string
  - Description: Name of the used counter electrode  
- reference_electrode
  - Type: ReferenceElectrode
  - Description: Name of the used reference electrode
- reference_electrode_salt
  - Type: string
  - Description: Name of the reference salt
- reference_electrode_salt_concentration
  - Type: float
  - Description: Unit of the reference salt concentration
- reference_electrode_salt_concentration_unit
  - Type: ConcentrationUnits
  - Description: Unit of the reference salt concentration

### Author

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
### Experiment_type
```python
CV = "CV"
CP = "CP"
CA = "CA"
```
### ChargeDensityUnits

``` python
COULOMB_PER_CUBIC_METER = "C/m^3"
```

### PressureUnits

```python
PASCAL = "Pa "
BAR = "bar"
MILLI_BAR = "mbar"
```

### MolecularWeightUnits

```python
GRAM_PER_MOLE = "g/mole "
GRAM_PER_MILLI_MOLE = "g/mmole"
```

### TemperatureUnits

```python
CELCIUS = "C"
KELVIN = "K"
```

### VolumeUnits

```python
MILLI_LITER = "ml"
MICRO_LITER = "µl" 
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
MOLAR = "M"
MILLI_MOLAR = "mM"
MICRO_MOLAR = "µM"
NANO_MOLAR = "nM"
GRAM_LITER = "g/l"
MILLIGRAM_LITER = "mg/l"
MICROGRAM_LITER = "ug/l"
NANGRAM_LITER = "ng/l"
```

### ScanRateUnits

```python
VOLT_PER_SEC = "V/s"
MILLI_VOLT_PER_SEC = "mV/s"
MICRO_VOLT_PER_SEC = "uV/s"
```

### CurrentUnits

```python
AMPERE = "A"
MILLI_AMPERE = "mA"
MICRO_AMPERE = "µA"
NANO_AMPERE = "nA"
```

### PotentialUnits

```python
VOLT = "V"
MILLI_VOLT = "mV"
MICRO_VOLT = "µV"
NANO_VOLT = "nV"
```
### AreaUnits

```python
SQUARE_CM= "cm^2"
SQUARE_MILLI_M = "mm^2"
```
### ReferenceElectrode
```python
SHE= "SHE"
RHE = "RHE"
Ag_AgCl= "Ag/AgCl"
Ag_AgSO4="Ag/Ag2SO4"
Hg_HgO="Hg/HgO"
Hg_Hg2Cl2="Hg/Hg2Cl2"
Hg_Hg2SO4="Hg/Hg2SO4"
Fc_Fc="Fc/Fc+"
```