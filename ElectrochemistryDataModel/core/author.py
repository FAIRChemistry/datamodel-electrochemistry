import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Author(sdRDM.DataModel):

    """Container for information regarding persons who worked on a dataset."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("authorINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Full name of the author",
    )

    affiliation: str = Field(
        ...,
        description="Organization the author is affiliated with",
    )

    email: Optional[str] = Field(
        default=None,
        description="Contact e-mail address of the author",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="723b7621cb273f11a5d3bf188d93df0af6426495"
    )
