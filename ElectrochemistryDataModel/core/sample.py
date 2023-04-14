import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .film_preparation import Film_preparation
from .synthesis import Synthesis
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

    chemical_formula: str = Field(
        ...,
        description="The chemical formula of the product",
    )

    molecular_weight: Molecular_weight_units = Field(
        ...,
        description="The molecular weight of the product",
    )

    synthesis: Synthesis = Field(
        ...,
        description="The synthesis of the product",
    )

    film_preparation: Film_preparation = Field(
        ...,
        description="The film preparation of the product",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="6554a2e922d0b3b07b953d3e331372ff9b7ec468"
    )
