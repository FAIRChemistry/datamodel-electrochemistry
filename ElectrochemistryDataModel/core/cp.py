import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


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

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="a9cad9dbb771ff3b79882ed4386148d229bb9c71"
    )
