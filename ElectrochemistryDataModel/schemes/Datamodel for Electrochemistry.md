```mermaid
classDiagram
    Dataset *-- Parameter
    
    class Dataset {
        +string name*
        +date date*
        +Parameter[0..*] parameter*
    }
    
    class Author {
        +string name*
    }
    
    class Parameter {
        +string solvent*
        +string conducting_salt*
        +int scan_rate*
        +string working_electrode*
        +string reference*
    }
    
    class Units {
        << Enumeration >>
        +VOLTAGE = "V"
        +AMPERE = "I"
    }
    
```