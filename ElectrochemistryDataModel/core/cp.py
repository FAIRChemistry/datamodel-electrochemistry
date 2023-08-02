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

    change_potential: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "A list of potential values, which could be used to transform reference"
            " potential scale"
        ),
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="32407172e3bb02a3b0d7ef553c1bed6f4e9badc7"
    )
