import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from datetime import date

from .author import Author


@forge_signature
class GeneralInformation(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("generalinformationINDEX"),
        xml="@id",
    )

    title: Optional[str] = Field(
        default=None,
        description="The title of the work",
    )

    author: List[Author] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Persons who worked on the dataset",
    )

    date_of_work: Optional[date] = Field(
        default=None,
        description="Date/time when the dataset was created",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="ce235b09a292fbf86d3ec367d054958dbe6889e1"
    )

    def add_to_author(
        self,
        name: Optional[str] = None,
        affiliation: Optional[str] = None,
        email: Optional[str] = None,
        orcid: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Author' to attribute author

        Args:
            id (str): Unique identifier of the 'Author' object. Defaults to 'None'.
            name (): Full name of the author. Defaults to None
            affiliation (): Organization the author is affiliated with. Defaults to None
            email (): Contact e-mail address of the author. Defaults to None
            orcid (): The ORCID of the author. Defaults to None
        """

        params = {
            "name": name,
            "affiliation": affiliation,
            "email": email,
            "orcid": orcid,
        }

        if id is not None:
            params["id"] = id

        self.author.append(Author(**params))
