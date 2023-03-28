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