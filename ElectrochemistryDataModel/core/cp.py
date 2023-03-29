import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .concentration_units import Concentration_units
from .time_units import Time_units
from .potential_units import Potential_units


@forge_signature
class CP(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cpINDEX"),
        xml="@id",
    )

    electrode_material: str = Field(
        ...,
        description="Name of the used electrode material",
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

    potential_first: Potential_units = Field(
        ...,
        description="The first induced potential",
    )

    potential_second: Potential_units = Field(
        ...,
        description="The second induced potential",
    )

    time_duration: Time_units = Field(
        ...,
        description="The time duration of the potential",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="32d178071e5fb3a810cab716ec136f2683546f94"
    )
