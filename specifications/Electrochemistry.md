# Datamodel for Electrochemistry
 
### Dataset

+ name* 
  + Type: string
  + Description: Name of the dataset

+ date*
  + Type: datetime
  + Default_factory: datetime.now
  + Description: Date/time when the dataset was created
+ parameter*
  + Type: Parameter
  + Multiple: True
  + Description: Name of the parameter
  
### Author
Container for information regarding persons who worked on a dataset.

+ name*
  + Type: string
  + Description: Full name of the author

### Parameters
Container for information regarding the CV-Setup and parameters

+ solvent*
  + Type: string
  + Description: Name of the solvent    
+ conducting salt*
  + Type: string
  + Description: Name of the used salt
+ scan rate*
  + Type: string
  + Description: Name of the used scan rate 
+  working electrode*
   + Type: string
   + Description: Name of the used working electrode
+ reference*
+ Type: string
+ Description: Name of the reference
  

Units
```python
VOLTAGE = "V"
AMPERE = "I"
```