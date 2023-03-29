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
        default="a21291b5dfb651f21de54ccf3046d77ebb56df90"
    )
