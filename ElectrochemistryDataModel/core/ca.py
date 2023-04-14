import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .potential_units import Potential_units
from .current_units import Current_units
from .time_units import Time_units


@forge_signature
class CA(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("caINDEX"),
        xml="@id",
    )

    induced_potential_first: Potential_units = Field(
        ...,
        description="The first induced potential",
    )

    induced_potential_second: Potential_units = Field(
        ...,
        description="The second induced potential",
    )

    time_duration: Time_units = Field(
        ...,
        description="The duration time of the induced potential",
    )

    current_end_value: Current_units = Field(
        ...,
        description="The current value at the end of the measurement",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0aa8beaf1f7d7a9a3e2dcefc9d4c1fb735a1df97"
    )
