import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .cp import CP
from .ca import CA
from .cv import CV


@forge_signature
class Analysis(sdRDM.DataModel):

    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("analysisINDEX"),
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
        default="122b947ee62a907093952580635d1c9eea3881a6"
    )
