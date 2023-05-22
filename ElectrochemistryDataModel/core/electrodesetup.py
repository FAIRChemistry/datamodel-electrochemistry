import sdRDM

from typing import Optional, Union, List
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator



@forge_signature
class ElectrodeSetup(sdRDM.DataModel):

                
    """"""
    
    id: str = Field(
            description="Unique identifier of the given object.",
            default_factory=IDGenerator("electrodesetupINDEX"),
            xml="@id"
    )
    
    WE: Optional[str] = Field(
    
    
    default=None,
    
    description="Name of the used working electrode",
    
    )

    CE: Optional[str] = Field(
    
    
    default=None,
    
    description="Name of the used counter electrode",
    
    )

    RE: Optional[str] = Field(
    
    
    default=None,
    
    description="Name of the used reference electrode",
    
    )

    RE_salt:: Optional[str] = Field(
    
    
    default=None,
    
    description="Name of the refererence salt",
    
    )

    __repo__: Optional[str] = PrivateAttr(default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git")
    __commit__: Optional[str] = PrivateAttr(default="beca177b218acaffb6190e8f60815c5bd7ce553e")
    

