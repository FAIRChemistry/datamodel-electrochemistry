import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .temperature_units import Temperature_units
from .time_units import Time_units
from .pressure_units import Pressure_units


@forge_signature
class Physical_parameters(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("physical_parametersINDEX"),
        xml="@id",
    )

    temperature: Temperature_units = Field(
        ...,
        description="The used temperature for the synthesis",
    )

    pressure: Pressure_units = Field(
        ...,
        description="The used pressure for the synthesis",
    )

    time: Time_units = Field(
        ...,
        description="The used time for the synthesis",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0aa8beaf1f7d7a9a3e2dcefc9d4c1fb735a1df97"
    )
