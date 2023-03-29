import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


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

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="08f0cd23a355152e3fc4211f5cdcbcad3355695a"
    )
