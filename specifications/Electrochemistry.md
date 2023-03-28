# Datamodel for Electrochemistry
 
### Dataset
- __name*__ 
  - Type: string
  - Description: Name of the dataset
- __date__
  - Type: date
  - Description: Date/time when the dataset was created
- __parameter*__
  - Type: Parameter
  - Multiple: True
  - Description: Name of the parameter
- __author__
  - Type: Author
  - Multiple: True
  - Description: Persons who worked on the dataset
  
### Author
Container for information regarding persons who worked on a dataset.

- __name__
  - Type: string
  - Description: Full name of the author
- __affiliation__
  - Type: string
  - Description: Organisation the author is affiliated with
- __email__
  - Type: string
  - Description: Contact e-mail address of the author
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
``` 