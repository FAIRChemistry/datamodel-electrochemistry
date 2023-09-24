import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .cv import CV
from .ca import CA
from .cp import CP


@forge_signature
class Analysis(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("analysisINDEX"),
        xml="@id",
    )

    cp: Optional[CP] = Field(
        default=None,
        description="Chronopotentiometry",
    )

    ca: Optional[CA] = Field(
        default=None,
        description="Chronoamperometry",
    )

    cv: Optional[CV] = Field(
        default=None,
        description="Cyclic Voltammetry",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="418b6230fb2c65662a83c99ad901093819dabeff"
    )
