import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .volume_units import Volume_units
from .temperature_units import Temperature_units
from .time_units import Time_units


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

    annealing_temperature: Optional[Temperature_units] = Field(
        default=None,
        description="The annealing temperature for the film",
    )

    annealing_time: Optional[Time_units] = Field(
        default=None,
        description="The annealing time for the film",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="291a9ade199207bc15bada70ebbff243eb8f3f8e"
    )
