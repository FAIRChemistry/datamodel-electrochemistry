import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class PeaksAndHalfPotential(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("peaksandhalfpotentialINDEX"),
        xml="@id",
    )

    current_maximum: Optional[float] = Field(
        default=None,
        description="A list of the peak maxima",
    )

    current_minimum: Optional[float] = Field(
        default=None,
        description="A list of the peak minima",
    )

    potential_maximum: Optional[float] = Field(
        default=None,
        description="A list of the peak maxima",
    )

    potential_minimum: Optional[float] = Field(
        default=None,
        description="A list of the peak minima",
    )

    current_unit: Optional[str] = Field(
        default=None,
        description="A list of the peak minima",
    )

    change_reference_potential: Optional[float] = Field(
        default=None,
        description="A list of the peak minima",
    )

    half_wave_potential: Optional[float] = Field(
        default=None,
        description="The half-wave potential of the measurement",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="204ff14b212a99bcf9201c31aee166048979bf02"
    )
