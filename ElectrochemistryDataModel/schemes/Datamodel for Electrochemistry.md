```mermaid
classDiagram
    Dataset *-- Author
    Dataset *-- Analysis
    
    class Dataset {
        +string name
        +date date
        +Author[0..*] author
        +Analysis analysis
    }
    
    class Analysis {
        +string cv
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