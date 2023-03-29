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

    potential_first: Potential_units = Field(
        ...,
        description="First potential which was used",
    )

    potential_sec: Potential_units = Field(
        ...,
        description="Second potential which was used",
    )

    time_between_switch: Time_units = Field(
        ...,
        description="The time between switching the potentials",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="def7541a119af366e3a906ab3b92245081af3799"
    )
