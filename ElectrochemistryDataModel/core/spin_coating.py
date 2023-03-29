import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .time_units import Time_units
from .temperature_units import Temperature_units
from .volume_units import Volume_units


@forge_signature
class Spin_coating(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("spin_coatingINDEX"),
        xml="@id",
    )

    volume: Volume_units = Field(
        ...,
        description="The volume which was used for the film",
    )

    rotation: float = Field(
        ...,
        description="The rotation speed for the film",
    )

    time: Time_units = Field(
        ...,
        description="The rotation time",
    )

    annealing_temperature: Temperature_units = Field(
        ...,
        description="The anealing temperature for the film",
    )

    annealing_time: Time_units = Field(
        ...,
        description="The anealing time for the film",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="d16fe602160546e991642e771d00e8ef338b6b94"
    )
