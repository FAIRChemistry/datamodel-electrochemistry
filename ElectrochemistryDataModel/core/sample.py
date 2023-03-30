import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .molecular_weight_units import Molecular_weight_units
from .synthesis import Synthesis
from .film_preparation import Film_preparation


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

    chemical_formula: Optional[str] = Field(
        default=None,
        description="The chemical formula of the product",
    )

    molecular_weight: Optional[Molecular_weight_units] = Field(
        default=None,
        description="The molecular weight of the product",
    )

    synthesis: Optional[Synthesis] = Field(
        default=None,
        description="The synthesis of the product",
    )

    film_preparation: Optional[Film_preparation] = Field(
        default=None,
        description="The film preparation of the product",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="d9cb4121a5423868bf2be4b646c847caba79c401"
    )
