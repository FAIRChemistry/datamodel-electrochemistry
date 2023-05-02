import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .currentunits import CurrentUnits
from .potentialunits import PotentialUnits
from .timeunits import TimeUnits
from .chargedensityunits import ChargeDensityUnits


@forge_signature
class CP(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cpINDEX"),
        xml="@id",
    )

    induced_current_first: Optional[CurrentUnits] = Field(
        default=None,
        description="The first induced current",
    )

    induced_current_second: Optional[CurrentUnits] = Field(
        default=None,
        description="The first induced current",
    )

    time_duration: Optional[TimeUnits] = Field(
        default=None,
        description="The duration time of the induced current",
    )

    potential_end_value: Optional[PotentialUnits] = Field(
        default=None,
        description="The potential value at the end of the measurement",
    )

    charge_density: List[ChargeDensityUnits] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The charge density of the measurement",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c2923491d3eaa0ef70e8ee712e5e55d7f9898d2a"
    )
