import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .timeunits import TimeUnits
from .temperatureunits import TemperatureUnits
from .pressureunits import PressureUnits


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
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="bf932f16222ff26e3bfe2c69151523db7c2ac916"
    )
