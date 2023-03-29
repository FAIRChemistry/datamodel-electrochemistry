import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .temperature_units import Temperature_units


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
        description="The temperature of the synthesis",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="08f0cd23a355152e3fc4211f5cdcbcad3355695a"
    )
