import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .charge_density_units import charge_density_units
from .potential_units import Potential_units
from .time_units import Time_units
from .current_units import Current_units


@forge_signature
class CP(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cpINDEX"),
        xml="@id",
    )

    induced_current_first: Current_units = Field(
        ...,
        description="The first induced current",
    )

    induced_current_second: Optional[Current_units] = Field(
        default=None,
        description="The first induced current",
    )

    time_duration: Time_units = Field(
        ...,
        description="The duration time of the induced current",
    )

    potential_end_value: Optional[Potential_units] = Field(
        default=None,
        description="The potential value at the end of the measurement",
    )

    charge_density: Optional[charge_density_units] = Field(
        default=None,
        description="The charge density of the measurement",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="4eea0b28792bb1fc20515eaf7d212d761f0a56ce"
    )
