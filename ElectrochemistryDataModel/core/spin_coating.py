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
        default="d9cb4121a5423868bf2be4b646c847caba79c401"
    )
