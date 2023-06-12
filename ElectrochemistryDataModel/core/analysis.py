import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .cp import CP
from .cv import CV
from .ca import CA


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
        default="cb12f3561b0b49f85f04d80dd56ea6af4d04f764"
    )
