# Datamodel for Electrochemistry
 
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
- __analysis__
  - Type: Analysis
  - Description: The method which is used to gain the data 


### Analysis
- __cv__
  - Type: CV
  - Multiple: True
  - Description: cv
  
### CV
Container for information regarding the CV-Setup and parameters
- __solvent__
  - Type: string
  - Description: Name of the solvent    
- __conducting_salt__
  - Type: string
  - Description: Name of the used salt
- __conducting_salt_concentration__
  - Type: float
  - Description: Concentration of the conducting salt in mol/l

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




  

#### Units
```python
VOLTAGE = "V"
AMPERE = "I"
``` 
