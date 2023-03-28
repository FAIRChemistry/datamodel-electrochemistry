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
  - Type: string
  - Description: This is a test 


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
``` 
