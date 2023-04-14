import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .timeunits import TimeUnits
from .potentialunits import PotentialUnits
from .currentunits import CurrentUnits
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
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="22aa1141fa295d3c23ead623d58474e96dcaf13b"
    )
