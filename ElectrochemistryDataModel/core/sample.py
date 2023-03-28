import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class Sample(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("sampleINDEX"),
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
        default="0627d0403a37c9162e0946dfdd475759f6682aac"
    )
