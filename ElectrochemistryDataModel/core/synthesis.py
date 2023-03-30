import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .physical_parameters import Physical_parameters


@forge_signature
class Synthesis(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("synthesisINDEX"),
        xml="@id",
    )

    reagents: str = Field(
        ...,
        description="The reagents of the product",
    )

    solvent: Optional[str] = Field(
        default=None,
        description="The solvent of the synthesis",
    )

    physical_parameters: Optional[Physical_parameters] = Field(
        default=None,
        description="The physical parameters of the synthesis",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="9818d0653ae6c5c6e71458e2c0594f3e8a947ec3"
    )
