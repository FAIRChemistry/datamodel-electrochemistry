import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class ElectrodeSetup(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("electrodesetupINDEX"),
        xml="@id",
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

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="016fed165461621b6366253dc9ac50f9b0ca8b52"
    )
