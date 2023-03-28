import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Sample(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("sampleINDEX"),
        xml="@id",
    )

    name: Optional[str] = Field(description="The name of the product", default=None)

    chemical_formula: Optional[str] = Field(
        description="The chemical formula of the product", default=None
    )

    synthesis: Optional[str] = Field(
        description="The synthesis of the product", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="c11230660bb1ac2ecc6100d0e3d62f5489172bd0"
    )
