import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Parameter(sdRDM.DataModel):
    """Container for information regarding the CV-Setup and parameters"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("parameterINDEX"),
        xml="@id",
    )

    solvent: str = Field(..., description="Name of the solvent")

    conducting_salt: str = Field(..., description="Name of the used salt")

    scan_rate: int = Field(..., description="Name of the used scan rate")

    working_electrode: str = Field(
        ..., description="Name of the used working electrode"
    )

    reference: str = Field(..., description="Name of the reference")

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="51895a81cf68d0ad170cee3cd6f1d9fca991cc9e"
    )
