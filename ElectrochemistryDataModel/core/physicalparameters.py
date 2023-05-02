import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .temperatureunits import TemperatureUnits
from .timeunits import TimeUnits
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
        default="522e0c5e9cc3081b74a6acdc2ca26ef673f987b0"
    )
