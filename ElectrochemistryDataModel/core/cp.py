import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class CP(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cpINDEX"),
        xml="@id",
    )

    solvent: Optional[str] = Field(description="Name of the solvent", default=None)

    conducting_salt: Optional[str] = Field(
        description="Name of the used salt", default=None
    )

    conducting_salt_concentration: Optional[float] = Field(
        description="Concentration of the conducting salt in mol/l", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="c11230660bb1ac2ecc6100d0e3d62f5489172bd0"
    )
