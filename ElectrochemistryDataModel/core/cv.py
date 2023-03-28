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

    conducting_salt_concentration: Optional[float] = Field(
        description="The half-wave potential of the measurement in V", default=None
    )

    scan_rate: Optional[float] = Field(
        description="The scan rate of the measurement in mV/s", default=None
    )

    i_pc: Optional[float] = Field(
        description="The current at the maximum of the cathodic peak in A", default=None
    )

    i_pa: Optional[float] = Field(
        description="The current at the maximum of the anodic peak in A", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="3b2ff760caea088f6a765fe8498dd9ccea93167d"
    )
