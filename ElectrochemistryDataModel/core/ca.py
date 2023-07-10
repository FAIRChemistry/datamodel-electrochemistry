import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .currentunits import CurrentUnits
from .timeunits import TimeUnits
from .potentialunits import PotentialUnits


@forge_signature
class CA(sdRDM.DataModel):

    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("caINDEX"),
        xml="@id",
    )

    measurement_current_unit: Optional[CurrentUnits] = Field(
        default=None,
        description="The current unit of the measurement",
    )

    measurement_time_unit: Optional[TimeUnits] = Field(
        default=None,
        description="The time unit of the measurement",
    )

    induced_potential: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The induced current",
    )

    induced_potential_unit: Optional[PotentialUnits] = Field(
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

    current_end_value: Optional[CurrentUnits] = Field(
        default=None,
        description="The current value at the end of the measurement",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="3de21a829fdaca4b3d164bfc43164bab1645da2e"
    )
