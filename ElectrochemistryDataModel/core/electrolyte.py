import sdRDM

from typing import Optional, Union
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

    conducting_salt_concentration: Union[float, str, None] = Field(
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
        default="cb390714d6b6eb8ab09b6299c7b2dcd2ee05c7f9"
    )
