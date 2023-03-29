import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .film_preparation import Film_preparation
from .molecular_weight_units import Molecular_weight_units


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

    synthesis: Optional[str] = Field(
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
        default="74f1d2bd51945e4f923c4bdc69721a8af615999c"
    )
