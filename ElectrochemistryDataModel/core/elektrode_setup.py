import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Elektrode_setup(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("elektrode_setupINDEX"),
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
        default="f7bda00987d9745b6e532491534c6fb55777ff96"
    )