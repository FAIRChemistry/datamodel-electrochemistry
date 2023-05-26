import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .concentrationunits import ConcentrationUnits


@forge_signature
class ElectrodeSetup(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("electrodesetupINDEX"),
        xml="@id",
    )

    CE: Optional[str] = Field(
        default=None,
        description="Name of the used counter electrode",
    )

    RE: Optional[str] = Field(
        default=None,
        description="Name of the used reference electrode",
    )

    RE_salt: Optional[str] = Field(
        default=None,
        description="Name of the reference salt",
    )

    RE_salt_concentration: Optional[float] = Field(
        default=None,
        description="Unit of the reference salt concentration",
    )

    RE_salt_concentration_unit: Optional[ConcentrationUnits] = Field(
        default=None,
        description="Unit of the reference salt concentration",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="915d216b340acec297c77e9d00eb9f0ab14862c5"
    )
