import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Author(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("authorINDEX"),
        xml="@id",
    )

    name: Optional[str] = Field(
        default=None,
        description="Full name of the author",
    )

    affiliation: Optional[str] = Field(
        default=None,
        description="Organization the author is affiliated with",
    )

    email: Optional[str] = Field(
        default=None,
        description="Contact e-mail address of the author",
    )

    orcid: Optional[str] = Field(
        default=None,
        description="The ORCID of the author",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="a25f65d2ce47b9591676df1cae2c224bb34e41ba"
    )
