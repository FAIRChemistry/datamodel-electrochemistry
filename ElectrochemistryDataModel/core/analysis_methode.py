import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .cp import CP
from .ca import CA
from .cv import CV


@forge_signature
class Analysis_methode(sdRDM.DataModel):

    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("analysis_methodeINDEX"),
        xml="@id",
    )

    cv: Optional[CV] = Field(
        default=None,
        description="Cyclic voltammetry",
    )

    ca: Optional[CA] = Field(
        default=None,
        description="Chronoamperometry",
    )

    cp: Optional[CP] = Field(
        default=None,
        description="Chronopotentiometry",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="104c20baf27e49c578eb70468cffff3483cad6f0"
    )
