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

    first_name: Optional[str] = Field(
        default=None,
        description="First name of the author",
    )

    last_name: Optional[str] = Field(
        default=None,
        description="Last name of the author",
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
        default="9c299403939a70a9a7b948024df737c1fcba5cac"
    )
