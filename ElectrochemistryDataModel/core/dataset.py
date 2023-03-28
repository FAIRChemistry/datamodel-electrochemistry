import sdRDM

from typing import Optional, Union
from typing import List
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from datetime import datetime
from .author import Author
from .analysis import Analysis


@forge_signature
class Dataset(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("datasetINDEX"),
        xml="@id",
    )

    date: Optional[datetime] = Field(
        description="Date/time when the dataset was created", default=None
    )

    author: List[Author] = Field(
        description="Persons who worked on the dataset", default_factory=ListPlus
    )

    name: Optional[str] = Field(description="Name of the dataset", default=None)

    analysis: Optional[Analysis] = Field(
        description="The method which is used to gain the data", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="3b5c2630d69c796efdc4772cbce3431cacf616ce"
    )

    def add_to_author(
        self,
        name: Optional[str] = None,
        affiliation: Optional[str] = None,
        email: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Author' to the attribute 'author'.

        Args:


            id (str): Unique identifier of the 'Author' object. Defaults to 'None'.


            name (Optional[str]): Full name of the author. Defaults to None


            affiliation (Optional[str]): Organisation the author is affiliated with. Defaults to None


            email (Optional[str]): Contact e-mail address of the author. Defaults to None
        """

        params = {"name": name, "affiliation": affiliation, "email": email}
        if id is not None:
            params["id"] = id
        author = [Author(**params)]
        self.author = self.author + author
