import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class CV(sdRDM.DataModel):
    """Container for information regarding the CV-Setup and parameters"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cvINDEX"),
        xml="@id",
    )

    solvent: Optional[str] = Field(description="Name of the solvent", default=None)

    conducting_salt: Optional[str] = Field(
        description="Name of the used salt", default=None
    )

    conducting_salt_c: Optional[float] = Field(
        description="Concentration of the conducting salt in mol/l", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="f85e3718a57a3c8617ff82c83b9645671501b4f7"
    )
