import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .time_units import Time_units
from .potential_units import Potential_units
from .current_units import Current_units
from .charge_density_units import Charge_density_units


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

    induced_current_second: Current_units = Field(
        ...,
        description="The first induced current",
    )

    time_duration: Time_units = Field(
        ...,
        description="The duration time of the induced current",
    )

    potential_end_value: Potential_units = Field(
        ...,
        description="The potential value at the end of the measurement",
    )

    charge_density: List[Charge_density_units] = Field(
        multiple=True,
        description="The charge density of the measurement",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0aa8beaf1f7d7a9a3e2dcefc9d4c1fb735a1df97"
    )
