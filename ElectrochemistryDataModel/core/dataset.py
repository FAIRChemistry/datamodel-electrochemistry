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
from .sample import Sample


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

    sample: List[Sample] = Field(
        description="The sample which was measured", default_factory=ListPlus
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="f6393eb24eff9440f2b245ef0bb7e2a4bc99ae9a"
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


            affiliation (Optional[str]): Organization the author is affiliated with. Defaults to None


            email (Optional[str]): Contact e-mail address of the author. Defaults to None
        """

        params = {"name": name, "affiliation": affiliation, "email": email}
        if id is not None:
            params["id"] = id
        author = [Author(**params)]
        self.author = self.author + author

    def add_to_sample(
        self,
        name: Optional[str] = None,
        chemical_formula: Optional[str] = None,
        synthesis: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Sample' to the attribute 'sample'.

        Args:


            id (str): Unique identifier of the 'Sample' object. Defaults to 'None'.


            name (Optional[str]): The name of the product. Defaults to None


            chemical_formula (Optional[str]): The chemical formula of the product. Defaults to None


            synthesis (Optional[str]): The synthesis of the product. Defaults to None
        """

        params = {
            "name": name,
            "chemical_formula": chemical_formula,
            "synthesis": synthesis,
        }
        if id is not None:
            params["id"] = id
        sample = [Sample(**params)]
        self.sample = self.sample + sample
