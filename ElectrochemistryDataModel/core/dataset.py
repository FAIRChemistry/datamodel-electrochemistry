import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from datetime import date

from .author import Author
from .sample import Sample
from .analysis import Analysis


@forge_signature
class Dataset(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("datasetINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Name of the dataset",
    )

    date: date = Field(
        ...,
        description="Date/time when the dataset was created",
    )

    author: List[Author] = Field(
        multiple=True,
        description="Persons who worked on the dataset",
        default_factory=ListPlus,
    )

    sample: List[Sample] = Field(
        multiple=True,
        description="The sample which was measured",
        default_factory=ListPlus,
    )

    electrode_material: str = Field(
        ...,
        description="Name of the used electrode material",
    )

    analysis: Analysis = Field(
        ...,
        description="The method which is used to gain the data",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="f6918b4f10c381590c3c63a5e6f0408c1e27775e"
    )

    def add_author_to_author(
        self,
        name: str,
        affiliation: str,
        email: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Author' to attribute author

        Args:
            id (str): Unique identifier of the 'Author' object. Defaults to 'None'.
            name (): Full name of the author.
            affiliation (): Organization the author is affiliated with.
            email (): Contact e-mail address of the author. Defaults to None
        """

        params = {
            "name": name,
            "affiliation": affiliation,
            "email": email,
        }

        if id is not None:
            params["id"] = id

        self.author.append(Author(**params))

    def add_sample_to_sample(
        self, name: str, chemical_formula: str, synthesis: str, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'Sample' to attribute sample

        Args:
            id (str): Unique identifier of the 'Sample' object. Defaults to 'None'.
            name (): The name of the product.
            chemical_formula (): The chemical formula of the product.
            synthesis (): The synthesis of the product.
        """

        params = {
            "name": name,
            "chemical_formula": chemical_formula,
            "synthesis": synthesis,
        }

        if id is not None:
            params["id"] = id

        self.sample.append(Sample(**params))
