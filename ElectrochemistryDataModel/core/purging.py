import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .timeunits import TimeUnits


@forge_signature
class Purging(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("purgingINDEX"),
        xml="@id",
    )

    gas: Optional[str] = Field(
        default=None,
        description="The used purging gas",
    )

    purging_time: Optional[int] = Field(
        default=None,
        description="The purging time",
    )

    purging_time_unit: Optional[TimeUnits] = Field(
        default=None,
        description="The purging time unit",
    )

    purging_repeatitions: Optional[int] = Field(
        default=None,
        description="The number of times the purging is repeated",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="ca1fc8137246ee95cdfdb51d0daf188daf059f36"
    )
