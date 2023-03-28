import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class Product(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("productINDEX"),
        xml="@id",
    )
    name: Optional[str] = Field(
        description="The name of the product",
        default=None,
    )

    chemical_formula: Optional[str] = Field(
        description="The chemical formula of the product",
        default=None,
    )

    synthesis: Optional[str] = Field(
        description="The synthesis of the product",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="615441ab6cb6d376edde4cf0afb09fdbd20d2d34"
    )
