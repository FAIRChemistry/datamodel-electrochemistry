import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .purging import Purging
from .timeunits import TimeUnits
from .temperatureunits import TemperatureUnits
from .pressureunits import PressureUnits


@forge_signature
class Synthesis(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("synthesisINDEX"),
        xml="@id",
    )

    reagents: Optional[str] = Field(
        default=None,
        description="The reagents of the product",
    )

    solvent: Optional[str] = Field(
        default=None,
        description="The solvent of the synthesis",
    )

    reaction_time: Optional[float] = Field(
        default=None,
        description="The reaction time",
    )

    reaction_time_unit: Optional[TimeUnits] = Field(
        default=None,
        description="The reaction time",
    )

    reaction_temperature: Optional[float] = Field(
        default=None,
        description="The reaction temperature",
    )

    reaction_temperature_unit: Optional[TemperatureUnits] = Field(
        default=None,
        description="The reaction temperature unit",
    )

    reaction_pressure: Optional[float] = Field(
        default=None,
        description="The reaction pressure",
    )

    reaction_pressure_unit: Optional[PressureUnits] = Field(
        default=None,
        description="The reaction pressure unit",
    )

    purging: Optional[Purging] = Field(
        default=None,
        description="The purging information for the synthesis experiment",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="77a7042bf9b874e52d61bfd2279e0089580e09f5"
    )
