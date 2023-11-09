import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class ChangePotential(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("changepotentialINDEX"),
        xml="@id",
    )

    change_potential_value: Optional[float] = Field(
        default=None,
        description="The change potential value",
    )

    new_reference_scale_name: Optional[str] = Field(
        default=None,
        description="The new reference scale name",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="e38a84311a8ea08c702d1783cdb18badc2653aa8"
    )
