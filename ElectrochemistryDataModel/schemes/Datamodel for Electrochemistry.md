```mermaid
classDiagram
    Dataset *-- Author
    
    class Dataset {
        +string name
        +date date
        +Author[0..*] author
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