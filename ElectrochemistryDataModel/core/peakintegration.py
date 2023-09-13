import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class PeakIntegration(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("peakintegrationINDEX"),
        xml="@id",
    )

    lower_limit_potential: Optional[float] = Field(
        default=None,
        description="Name of the used working electrode",
    )

    upper_limit_potential: Optional[float] = Field(
        default=None,
        description="Name of the used working electrode",
    )

    integration_area: Optional[float] = Field(
        default=None,
        description="Name of the used working electrode",
    )

    integration_area_unit: Optional[str] = Field(
        default=None,
        description="Name of the used working electrode",
    )

    integration_direction: Optional[str] = Field(
        default=None,
        description="The integration direction.",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="1dbb322a6d12cf7b3c1a8d97cf3cd32f605007fd"
    )
