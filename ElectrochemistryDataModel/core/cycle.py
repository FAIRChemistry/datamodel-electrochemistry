import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Cycle(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cycleINDEX"),
        xml="@id",
    )

    cycles: List[int] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="A list of the cycles",
    )

    peak_maxima: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="A list of the peak maxima",
    )

    peak_minima: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="A list of the peak minima",
    )

    half_wave_potential: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The half-wave potential of the measurement",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="aa72e6ccad3122ff52737dcf8aef6844dc4b2ceb"
    )
