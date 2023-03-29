import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .time_units import Time_units
from .concentration_units import Concentration_units
from .potential_units import Potential_units


@forge_signature
class CA(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("caINDEX"),
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

    induced_potential_first: Potential_units = Field(
        ...,
        description="The first induced potential",
    )

    induced_potential_second: Potential_units = Field(
        ...,
        description="The second induced potential",
    )

    time_duration: Time_units = Field(
        ...,
        description="The duration time of the induced potential",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="dd1882d934bee8cce03649e97bbaa4b129ccff09"
    )
