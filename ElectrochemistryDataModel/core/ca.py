import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .potentialunits import PotentialUnits
from .timeunits import TimeUnits
from .currentunits import CurrentUnits


@forge_signature
class CA(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("caINDEX"),
        xml="@id",
    )

    induced_potential_first: Optional[PotentialUnits] = Field(
        default=None,
        description="The first induced potential",
    )

    induced_potential_second: Optional[PotentialUnits] = Field(
        default=None,
        description="The second induced potential",
    )

    time_duration: Optional[TimeUnits] = Field(
        default=None,
        description="The duration time of the induced potential",
    )

    current_end_value: Optional[CurrentUnits] = Field(
        default=None,
        description="The current value at the end of the measurement",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="5a92e279f78e2a843a6a0e9cfdb646b73c3e843c"
    )
