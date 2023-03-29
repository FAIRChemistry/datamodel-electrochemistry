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

    name_product: str = Field(
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
        default="a2c1245141f071cb3365890d65b3d05da7caaee3"
    )
