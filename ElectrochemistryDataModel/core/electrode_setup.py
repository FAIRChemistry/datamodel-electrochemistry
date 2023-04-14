import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Electrode_setup(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("electrode_setupINDEX"),
        xml="@id",
    )

    working_electrode: str = Field(
        ...,
        description="Name of the used working electrode",
    )

    counter_electrode: str = Field(
        ...,
        description="Name of the used counter electrode",
    )

    Reference_electrode: str = Field(
        ...,
        description="Name of the used reference electrode",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="6554a2e922d0b3b07b953d3e331372ff9b7ec468"
    )
