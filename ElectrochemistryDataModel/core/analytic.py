import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Analytic(sdRDM.DataModel):

    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("analyticINDEX"),
        xml="@id",
    )

    cyclic_v: Optional[str] = Field(
        default=None,
        description="Cyclic voltammetry test",
    )

    chrono_a: Optional[str] = Field(
        default=None,
        description="Chronoamperometry test",
    )

    chrono_p: Optional[str] = Field(
        default=None,
        description="Chronopotentiometry test",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="cb12f3561b0b49f85f04d80dd56ea6af4d04f764"
    )
