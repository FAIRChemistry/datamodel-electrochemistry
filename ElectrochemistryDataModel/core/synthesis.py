import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .physicalparameters import PhysicalParameters


@forge_signature
class Synthesis(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("synthesisINDEX"),
        xml="@id",
    )

    reagents: Optional[str] = Field(
        default=None,
        description="The reagents of the product",
    )

    solvent: Optional[str] = Field(
        default=None,
        description="The solvent of the synthesis",
    )

    physical_parameters: Optional[PhysicalParameters] = Field(
        default=None,
        description="The physical parameters of the synthesis",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="a25f65d2ce47b9591676df1cae2c224bb34e41ba"
    )
