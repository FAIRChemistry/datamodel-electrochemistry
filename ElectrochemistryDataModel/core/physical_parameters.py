import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .pressure_units import Pressure_units
from .temperature_units import Temperature_units
from .time_units import Time_units


@forge_signature
class Physical_parameters(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("physical_parametersINDEX"),
        xml="@id",
    )

    temperature: Optional[Temperature_units] = Field(
        default=None,
        description="The used temperature for the synthesis",
    )

    pressure: Optional[Pressure_units] = Field(
        default=None,
        description="The used pressure for the synthesis",
    )

    time: Optional[Time_units] = Field(
        default=None,
        description="The used time for the synthesis",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="480ec8ed2f5f9ef7130c63306c48e9ded43e9f46"
    )
