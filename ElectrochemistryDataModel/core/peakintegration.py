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
        default="a39428cabbbbcba7c89935626bf374b54c6f797a"
    )
