import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .potential_units import Potential_units
from .time_units import Time_units
from .concentration_units import Concentration_units


@forge_signature
class CP(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cpINDEX"),
        xml="@id",
    )

    solvent: str = Field(
        ...,
        description="Name of the solvent",
    )

    conducting_salt: str = Field(
        ...,
        description="Name of the used salt",
    )

    conducting_salt_concentration: Concentration_units = Field(
        ...,
        description="Concentration of the conducting salt",
    )

    potential_start: Potential_units = Field(
        ...,
        description="The potential where the measurement starts",
    )

    potential_stop: Potential_units = Field(
        ...,
        description="The potential where the measurement ends",
    )

    potential_lower_limit: Potential_units = Field(
        ...,
        description="The lower limit of the potential",
    )

    potential_upper_limit: Potential_units = Field(
        ...,
        description="The upper limit of the potential",
    )

    time_duration: Time_units = Field(
        ...,
        description="The time duration of the potential",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="bedb286cf489fcf39a63b25075c21d587b2f0558"
    )
