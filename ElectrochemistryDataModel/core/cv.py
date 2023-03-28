import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class CV(sdRDM.DataModel):

    """Container for information regarding the CV-Setup and parameters"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cvINDEX"),
        xml="@id",
    )
    solvent: Optional[str] = Field(
        description="Name of the solvent",
        default=None,
    )

    conducting_salt: Optional[str] = Field(
        description="Name of the used salt",
        default=None,
    )

    conducting_salt_c: Optional[float] = Field(
        description="Concentration of the conducting salt in mol/l",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="45ab805561cb30ec578fdf838617134280a81899"
    )
