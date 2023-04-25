import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .timeunits import TimeUnits
from .volumeunits import VolumeUnits
from .temperatureunits import TemperatureUnits


@forge_signature
class SpinCoating(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("spincoatingINDEX"),
        xml="@id",
    )

    volume: Optional[VolumeUnits] = Field(
        default=None,
        description="The volume which was used for the film",
    )

    rotation: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The rotation speed of the spin coating process",
    )

    time: Optional[TimeUnits] = Field(
        default=None,
        description="The rotation time",
    )

    annealing_temperature: Optional[TemperatureUnits] = Field(
        default=None,
        description="The annealing temperature for the film",
    )

    annealing_time: Optional[TimeUnits] = Field(
        default=None,
        description="The annealing time for the film",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="42a10df368466278a1eb48e7c227a53c81d99bb2"
    )
