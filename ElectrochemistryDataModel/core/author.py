import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Author(sdRDM.DataModel):
    """Container for information regarding persons who worked on a dataset."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("authorINDEX"),
        xml="@id",
    )

    name: Optional[str] = Field(description="Full name of the author", default=None)

    email: Optional[str] = Field(
        description="Contact e-mail address of the author", default=None
    )

    affiliation: Optional[str] = Field(
        description="Organization the author is affiliated with", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="fc2de33fd590747bac461de02563b771896f9ba7"
    )
