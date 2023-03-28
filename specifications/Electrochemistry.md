# Datamodel for Electrochemistry
 
### Dataset
- __name*__ 
  - Type: string
  - Description: Name of the dataset
- __date*__
  - Type: date
  - Description: Date/time when the dataset was created
- __parameter*__
  - Type: Parameter
  - Multiple: True
  - Description: Name of the parameter
  
### Author
Container for information regarding persons who worked on a dataset.

- __name*__
  - Type: string
  - Description: Full name of the author

### Parameter
Container for information regarding the CV-Setup and parameters

- __solvent*__
  - Type: string
  - Description: Name of the solvent    
- __conducting_salt*__
  - Type: string
  - Description: Name of the used salt
- __scan_rate*__
  - Type: int
  - Description: Name of the used scan rate 
- __working_electrode*__
  - Type: string
  - Description: Name of the used working electrode
- __reference*__
  - Type: string
  - Description: Name of the reference
  

#### Units
```python
VOLTAGE = "V"
AMPERE = "I"
``` 
