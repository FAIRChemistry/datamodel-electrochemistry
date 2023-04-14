import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .pressureunits import PressureUnits
from .timeunits import TimeUnits
from .temperatureunits import TemperatureUnits


@forge_signature
class PhysicalParameters(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("physicalparametersINDEX"),
        xml="@id",
    )

    temperature: Optional[TemperatureUnits] = Field(
        default=None,
        description="The used temperature for the synthesis",
    )

    pressure: Optional[PressureUnits] = Field(
        default=None,
        description="The used pressure for the synthesis",
    )

    time: Optional[TimeUnits] = Field(
        default=None,
        description="The used time for the synthesis",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="ecc85f48105a90034198f80e8b66b93159b9c5b8"
    )
