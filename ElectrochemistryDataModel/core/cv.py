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

    total_cycle_number: Optional[int] = Field(
        description="The total cycle number", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="fc2de33fd590747bac461de02563b771896f9ba7"
    )
