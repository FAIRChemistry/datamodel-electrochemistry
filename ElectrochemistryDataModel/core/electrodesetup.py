import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class ElectrodeSetup(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("electrodesetupINDEX"),
        xml="@id",
    )

    working_electrode: Optional[str] = Field(
        default=None,
        description="Name of the used working electrode",
    )

    counter_electrode: Optional[str] = Field(
        default=None,
        description="Name of the used counter electrode",
    )

    Reference_electrode: Optional[str] = Field(
        default=None,
        description="Name of the used reference electrode",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="ecc85f48105a90034198f80e8b66b93159b9c5b8"
    )
