import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
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

    rotation: List[float] = Field(
        multiple=True,
        description="The rotation speed of the spin coating process",
        default_factory=ListPlus,
    )

    time: Time_units = Field(
        ...,
        description="The rotation time",
    )

    annealing_temperature: Temperature_units = Field(
        ...,
        description="The annealing temperature for the film",
    )

    annealing_time: Time_units = Field(
        ...,
        description="The annealing time for the film",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="6554a2e922d0b3b07b953d3e331372ff9b7ec468"
    )
