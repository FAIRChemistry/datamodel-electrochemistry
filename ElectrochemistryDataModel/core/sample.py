import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .synthesis import Synthesis
from .filmpreparation import FilmPreparation
from .molecularweightunits import MolecularWeightUnits


@forge_signature
class Sample(sdRDM.DataModel):

    """"""

    id: str = Field(
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
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="20dbf0b641016843c2093cd6e5f46d991659add4"
    )
