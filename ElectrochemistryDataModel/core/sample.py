import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Sample(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("sampleINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="The name of the product",
    )

    chemical_formula: str = Field(
        ...,
        description="The chemical formula of the product",
    )

    synthesis: str = Field(
        ...,
        description="The synthesis of the product",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0e43514b8429bb85611734e1b552164136f060bc"
    )
