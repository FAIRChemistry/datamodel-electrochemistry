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
        default="f6e54ac9d2962ff8c21c9b063914e5cfd9433551"
    )
