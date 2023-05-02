import sdRDM

from typing import Optional, Union, List
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator



@forge_signature
class Dataset_for_plots(sdRDM.DataModel):

                
    """"""
    
    id: str = Field(
            description="Unique identifier of the given object.",
            default_factory=IDGenerator("dataset_for_plotsINDEX"),
            xml="@id"
    )
    
    filename: Optional[str] = Field(
    
    
    default=None,
    
    description="The filename with path",
    
    )

    reference: Optional[str] = Field(
    
    
    default=None,
    
    description="The reference",
    
    )

    name: Optional[str] = Field(
    
    
    default=None,
    
    description="The name",
    
    )

    conducting_salt: Optional[str] = Field(
    
    
    default=None,
    
    description="The conducting_salt",
    
    )

    concentration: Optional[str] = Field(
    
    
    default=None,
    
    description="The conducted_salt_concentration",
    
    )

    solvent: Optional[str] = Field(
    
    
    default=None,
    
    description="The solvent",
    
    )

    pH: Optional[str] = Field(
    
    
    default=None,
    
    description="The pH value",
    
    )

    scan_rate: Optional[str] = Field(
    
    
    default=None,
    
    description="The scan rate",
    
    )

    substrate: Optional[str] = Field(
    
    
    default=None,
    
    description="name of the substrate (WE)",
    
    )

    area_WE:: Optional[str] = Field(
    
    
    default=None,
    
    description="The area of the WE",
    
    )

    __repo__: Optional[str] = PrivateAttr(default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git")
    __commit__: Optional[str] = PrivateAttr(default="016fed165461621b6366253dc9ac50f9b0ca8b52")
    

