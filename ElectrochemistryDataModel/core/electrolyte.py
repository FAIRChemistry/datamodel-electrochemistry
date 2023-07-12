import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .concentrationunits import ConcentrationUnits


@forge_signature
class Electrolyte(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("electrolyteINDEX"),
        xml="@id",
    )

    solvent: Optional[str] = Field(
        default=None,
        description="Name of the solvent",
    )

    conducting_salt: Optional[str] = Field(
        default=None,
        description="Name of the used salt",
    )

    conducting_salt_concentration: Optional[float] = Field(
        default=None,
        description="Concentration of the conducting salt",
    )

    conducting_salt_concentration_unit: Optional[ConcentrationUnits] = Field(
        default=None,
        description="Unit of the conducting salt concentration",
    )

    pH: Optional[float] = Field(
        default=None,
        description="The pH value",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="f3ef752e4bbba633cbb9de1e24f76a05d6cf2b89"
    )
