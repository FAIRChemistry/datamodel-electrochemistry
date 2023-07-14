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

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cpINDEX"),
        xml="@id",
    )

    measurement_potential_unit: Optional[PotentialUnits] = Field(
        default=None,
        description="The potential unit of the measurement",
    )

    measurement_time_unit: Optional[TimeUnits] = Field(
        default=None,
        description="The time unit of the measurement",
    )

    induced_current: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The induced current",
    )

    induced_current_unit: Optional[CurrentUnits] = Field(
        default=None,
        description="The induced current unit",
    )

    time_duration: Optional[float] = Field(
        default=None,
        description="The duration time of the induced current",
    )

    time_duration_unit: Optional[TimeUnits] = Field(
        default=None,
        description="The duration time unit of the induced current",
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
        default="4e917b8a3743734f658746f6497e543d73ee5fe2"
    )
