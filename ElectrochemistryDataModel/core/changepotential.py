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
        default="9c299403939a70a9a7b948024df737c1fcba5cac"
    )
