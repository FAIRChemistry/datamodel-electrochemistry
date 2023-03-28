```mermaid
classDiagram
    Dataset *-- Author
    Dataset *-- Analysis
    Analysis *-- CV
    
    class Dataset {
        +string name
        +date date
        +Author[0..*] author
        +Analysis analysis
    }
    
    class Analysis {
        +CV[0..*] cv
    }
    
    class CV {
        +string solvent
        +string conducting_salt
        +float conducting_salt_concentration
        +float halfe_wave_potential
        +float scan_rate
        +float i_pc
        +float i_pa
        +float potential_E_pc
        +float potential_E_pa
        +int total_cycle_number
    }
    
    class Author {
        +string name
        +string affiliation
        +string email
    }
    
    class Units {
        << Enumeration >>
        +VOLTAGE = "V"
        +AMPERE = "I"
    }
    
```