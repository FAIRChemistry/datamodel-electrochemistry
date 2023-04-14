# Data model for Electrochemistry

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
  - Type: ConcentrationUnits
  - Description: Concentration of the conducting salt
- __electrode_setup__
  - Type: ElectrodeSetup
  - Description: Name of the used electrode materials

### Sample

- __name_product__
  - Type: string
  - Description: The name of the product
- __chemical_formula__
  - Type: string  
  - Description: The chemical formula of the product
- __molecular_weight__
  - Type: MolecularWeightUnits
  - Description: The molecular weight of the product
- __synthesis__
  - Type: Synthesis
  - Description: The synthesis of the product
- __film_preparation__
  - Type: FilmPreparation
  - Description: The film preparation of the product

### Synthesis

- __reagents__
  - Type: string
  - Description: The reagents of the product
- __solvent__
  - Type: string
  - Description: The solvent of the synthesis
- __physical_parameters__
  - Type: PhysicalParameters
  - Description: The physical parameters of the synthesis

### PhysicalParameters

- __temperature__
  - Type: TemperatureUnits
  - Description: The used temperature for the synthesis
- __pressure__
  - Type: PressureUnits
  - Description: The used pressure for the synthesis
- __time__
  - Type: TimeUnits
  - Description: The used time for the synthesis  

### FilmPreparation

- __spin_coating__
  - Type: SpinCoating
  - Multiple: True
  - Description: Spin coating parameter

### SpinCoating

- __volume__
  - Type: VolumeUnits
  - Description: The volume which was used for the film
- __rotation__
  - Type: float
  - Multiple: True
  - Description: The rotation speed of the spin coating process
- __time__
  - Type: TimeUnits
  - Description: The rotation time
- __annealing_temperature__
  - Type: TemperatureUnits
  - Description: The annealing temperature for the film
- __annealing_time__
  - Type: TimeUnits
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
  - Type: CurrentUnits
  - Description: The first induced current  
- __induced_current_second__
  - Type: CurrentUnits
  - Description: The first induced current  
- __time_duration__
  - Type: TimeUnits
  - Description: The duration time of the induced current
- __potential_end_value__
  - Type: PotentialUnits
  - Description: The potential value at the end of the measurement
- __charge_density__
  - Type: ChargeDensityUnits
  - Multiple: True
  - Description: The charge density of the measurement

### CA

- __induced_potential_first__
  - Type: PotentialUnits
  - Description: The first induced potential  
- __induced_potential_second__
  - Type: PotentialUnits
  - Description: The second induced potential
- __time_duration__
  - Type: TimeUnits
  - Description: The duration time of the induced potential
- __current_end_value__
  - Type: CurrentUnits
  - Description: The current value at the end of the measurement

### CV

Container for information regarding the CV-Setup and parameters

- __ferrocene_reference__
  - Type: Ferrocene_reference
  - Multiple: True
  - Description: Parameters of the ferocene reference measurement
- __halfe_wave_potential__
  - Type: PotentialUnits
  - Multiple: True
  - Description: The half-wave potential of the measurement  
- __scan_rate__
  - Type: ScanRateUnits
  - Description: The scan rate of the measurement
- __start_potential__
  - Type: PotentialUnits
  - Description: The starting value of the potential
- __stop_potential__
  - Type: PotentialUnits
  - Description: The stop value of the potential
- __potential_lower_limit__
  - Type: PotentialUnits
  - Description: The lower limit of the potential
- __potential_upper_limit__
  - Type: PotentialUnits
  - Description: The upper limit of the potential
- __i_pc_ox__
  - Type: CurrentUnits
  - Multiple: True
  - Description: The current at the maximum of the cathodic peak (oxidation)
- __i_pa_red__
  - Type: CurrentUnits
  - Multiple: True
  - Description: The current at the maximum of the anodic peak (reduction)
- __ox_potential_E_pc__
  - Type: PotentialUnits
  - Multiple: True
  - Description: Potential at the maximum of the cathodic peak (reduction)
- __red_potential_E_pa__
  - Type: PotentialUnits
  - Multiple: True
  - Description: The current at the maximum of the anodic peak (oxidation)
- __total_cycle_number__
  - Type: int
  - Description: The total cycle number

### Ferrocene_reference

- __ox_potential_E_pc_ferrocene__
  - Type: PotentialUnits
  - Description: Potential at the maximum of the cathodic peak (reduction) of the ferrocene reference
- __red_potential_E_pa_ferrocene__
  - Type: PotentialUnits
  - Description: The current at the maximum of the anodic peak (oxidation) of the ferrocene reference
- __halfe_wave_potential_ferrocene__
  - Type: PotentialUnits
  - Description: The half-wave potential of the ferrocene measurement

### ElectrodeSetup

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

#### ChargeDensityUnits

``` python
COULOMB_PER_CUBIC_METER = "C / m**3"
```

#### PressureUnits

```python
PASCAL = "Pa "
BAR = "bar"
MILLI_BAR = "mbar"
```

#### MolecularWeightUnits

```python
GRAM_PER_MOLE = "g / mole "
GRAM_PER_MILLI_MOLE = "g / mmole"
```

#### TemperatureUnits

```python
CELCIUS = "C"
KELVIN = "K"
```

#### VolumeUnits

```python
MILLI_LITER = "ml"
MICRO_LITER = "ul" 
NANO_LITER = "nl"
```

#### TimeUnits

```python
HOUR = "h"
MIN = "min"
SEC = "s" 
MILLI_SEC = "ms"
MICRO_SEC = "us"
```

#### ConcentrationUnits

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

#### ScanRateUnits

```python
VOLT_PER_SEC = "V / s"
MILLI_VOLT_PER_SEC = "mV / s"
MICRO_VOLT_PER_SEC = "uV / s"
```

#### CurrentUnits

```python
AMPERE = "A"
MILLI_AMPERE = "mA"
MICRO_AMPERE = "uA"
NANO_AMPERE = "nA"
```

#### PotentialUnits

```python
VOLT = "V"
MILLI_VOLT = "mV"
MICRO_VOLT = "uV"
NANO_VOLT = "nV"
```
