import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .filmpreparation import FilmPreparation
from .synthesis import Synthesis
from .molecularweightunits import MolecularWeightUnits


@forge_signature
class Sample(sdRDM.DataModel):

    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("sampleINDEX"),
        xml="@id",
    )

    name_product: Optional[str] = Field(
        default=None,
        description="The name of the product",
    )

    chemical_formula: Optional[str] = Field(
        default=None,
        description="The chemical formula of the product",
    )

    molecular_weight: Optional[MolecularWeightUnits] = Field(
        default=None,
        description="The molecular weight of the product",
    )

    synthesis: Optional[Synthesis] = Field(
        default=None,
        description="The synthesis of the product",
    )

    film_preparation: Optional[FilmPreparation] = Field(
        default=None,
        description="The film preparation of the product",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="396d0b56786086c8be6546c7ab4610c9ded2fbb1"
    )
