```mermaid
classDiagram
    Dataset *-- ConcentrationUnits
    Dataset *-- GeneralInformation
    Dataset *-- Experiment
    Dataset *-- Analysis_methode
    GeneralInformation *-- Author
    Experiment *-- Experiment_type
    Experiment *-- AreaUnits
    Experiment *-- Electrolyte
    Experiment *-- ElectrodeSetup
    Electrolyte *-- ConcentrationUnits
    Sample *-- MolecularWeightUnits
    Sample *-- Synthesis
    Sample *-- FilmPreparation
    Synthesis *-- PhysicalParameters
    PhysicalParameters *-- PressureUnits
    PhysicalParameters *-- TemperatureUnits
    PhysicalParameters *-- TimeUnits
    FilmPreparation *-- SpinCoating
    SpinCoating *-- TemperatureUnits
    SpinCoating *-- VolumeUnits
    SpinCoating *-- TimeUnits
    Analysis_methode *-- CP
    Analysis_methode *-- CA
    Analysis_methode *-- CV
    CP *-- ChargeDensityUnits
    CP *-- TimeUnits
    CP *-- CurrentUnits
    CP *-- PotentialUnits
    CP *-- Experiment
    CA *-- TimeUnits
    CA *-- CurrentUnits
    CA *-- PotentialUnits
    CA *-- Experiment
    CV *-- ScanRateUnits
    CV *-- CurrentUnits
    CV *-- PotentialUnits
    CV *-- Experiment
    ElectrodeSetup *-- ConcentrationUnits
    ElectrodeSetup *-- AreaUnits
    
    class Dataset {
        +GeneralInformation general_information
        +Analysis_methode analysis_methode
        +string solvent
        +string conducting_salt
        +float conducting_salt_concentration
        +ConcentrationUnits conducting_salt_concentration_unit
        +Experiment[0..*] experiments
    }
    
    class GeneralInformation {
        +string title
        +Author[0..*] author
        +date date_of_work
    }
    
    class Experiment {
        +string name
        +string filename
        +string WE_material
        +AreaUnits WE_area
        +string solvent_test
        +ElectrodeSetup electrode_setup
        +Electrolyte electrolyte
        +Experiment_type type
    }
    
    class Electrolyte {
        +string solvent
        +string conducting_salt
        +float conducting_salt_concentration
        +ConcentrationUnits conducting_salt_concentration_unit
    }
    
    class Sample {
        +string name_product
        +string chemical_formula
        +MolecularWeightUnits molecular_weight
        +Synthesis synthesis
        +FilmPreparation film_preparation
    }
    
    class Synthesis {
        +string reagents
        +string solvent
        +PhysicalParameters physical_parameters
    }
    
    class PhysicalParameters {
        +TemperatureUnits temperature
        +PressureUnits pressure
        +TimeUnits time
    }
    
    class FilmPreparation {
        +SpinCoating[0..*] spin_coating
    }
    
    class SpinCoating {
        +VolumeUnits volume
        +float[0..*] rotation
        +TimeUnits time
        +TemperatureUnits annealing_temperature
        +TimeUnits annealing_time
    }
    
    class Analysis_methode {
        +CV cv
        +CA ca
        +CP cp
    }
    
    class DatasetForPlots {
        +string filename
        +string reference
        +string name
        +string conducting_salt
        +string concentration
        +string solvent
        +string pH
        +string scan_rate
        +string substrate
    }
    
    class CP {
        +float[0..*] induced_current
        +CurrentUnits induced_current_unit
        +CurrentUnits induced_current_second
        +TimeUnits time_duration
        +PotentialUnits potential_end_value
        +ChargeDensityUnits[0..*] charge_density
        +Experiment[0..*] cp_experiments
    }
    
    class CA {
        +float induced_potential_first
        +PotentialUnits induced_potential_first_unit
        +PotentialUnits induced_potential_second
        +TimeUnits time_duration
        +CurrentUnits current_end_value
        +Experiment[0..*] ca_experiments
    }
    
    class CV {
        +Experiment[0..*] cp_experiments
        +PotentialUnits[0..*] half_wave_potential
        +ScanRateUnits scan_rate
        +PotentialUnits start_potential
        +PotentialUnits stop_potential
        +PotentialUnits potential_lower_limit
        +PotentialUnits potential_upper_limit
        +CurrentUnits[0..*] i_pc_ox
        +CurrentUnits[0..*] i_pa_red
        +PotentialUnits[0..*] ox_potential_E_pc
        +PotentialUnits[0..*] red_potential_E_pa
        +int total_cycle_number
    }
    
    class ElectrodeSetup {
        +string working_electrode
        +AreaUnits Working_electrode_area
        +string conter_electrode
        +string reference_electrode
        +string reference_electrode_salt
        +float reference_electrode_salt_concentration
        +ConcentrationUnits reference_electrode_salt_concentration_unit
    }
    
    class Author {
        +string name
        +string affiliation
        +string email
        +string orcid
    }
    
    class Experiment_type {
        << Enumeration >>
        +CV
        +CP
        +CA
    }
    
    class ChargeDensityUnits {
        << Enumeration >>
        +COULOMB_PER_CUBIC_METER
    }
    
    class PressureUnits {
        << Enumeration >>
        +PASCAL
        +BAR
        +MILLI_BAR
    }
    
    class MolecularWeightUnits {
        << Enumeration >>
        +GRAM_PER_MOLE
        +GRAM_PER_MILLI_MOLE
    }
    
    class TemperatureUnits {
        << Enumeration >>
        +CELCIUS
        +KELVIN
    }
    
    class VolumeUnits {
        << Enumeration >>
        +MILLI_LITER
        +MICRO_LITER
        +NANO_LITER
    }
    
    class TimeUnits {
        << Enumeration >>
        +HOUR
        +MIN
        +SEC
        +MILLI_SEC
        +MICRO_SEC
    }
    
    class ConcentrationUnits {
        << Enumeration >>
        +MOLAR
        +MILLI_MOLAR
        +MICRO_MOLAR
        +NANO_MOLAR
        +GRAM_LITER
        +MILLIGRAM_LITER
        +MICROGRAM_LITER
        +NANGRAM_LITER
    }
    
    class ScanRateUnits {
        << Enumeration >>
        +VOLT_PER_SEC
        +MILLI_VOLT_PER_SEC
        +MICRO_VOLT_PER_SEC
    }
    
    class CurrentUnits {
        << Enumeration >>
        +AMPERE
        +MILLI_AMPERE
        +MICRO_AMPERE
        +NANO_AMPERE
    }
    
    class PotentialUnits {
        << Enumeration >>
        +VOLT
        +MILLI_VOLT
        +MICRO_VOLT
        +NANO_VOLT
    }
    
    class AreaUnits {
        << Enumeration >>
        +SQUARE_CM
        +SQUARE_MILLI_M
    }
    
```