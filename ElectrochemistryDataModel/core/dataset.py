import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from datetime import date

from .sample import Sample
from .electrode_setup import Electrode_setup
from .concentration_units import Concentration_units
from .molecular_weight_units import Molecular_weight_units
from .author import Author
from .synthesis import Synthesis
from .analysis import Analysis
from .film_preparation import Film_preparation


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

    analysis: Analysis = Field(
        ...,
        description="The method which is used to gain the data",
    )

    solvent: str = Field(
        ...,
        description="Name of the solvent",
    )

    conducting_salt: str = Field(
        ...,
        description="Name of the used salt",
    )

    conducting_salt_concentration: Concentration_units = Field(
        ...,
        description="Concentration of the conducting salt",
    )

    electrode_setup: Electrode_setup = Field(
        ...,
        description="Name of the used electrode materials",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="9818d0653ae6c5c6e71458e2c0594f3e8a947ec3"
    )

    def add_author_to_author(
        self,
        name: str,
        affiliation: Optional[str] = None,
        email: Optional[str] = None,
        orcid: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Author' to attribute author

        Args:
            id (str): Unique identifier of the 'Author' object. Defaults to 'None'.
            name (): Full name of the author.
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

    def add_sample_to_sample(
        self,
        name_product: str,
        chemical_formula: Optional[str] = None,
        molecular_weight: Optional[Molecular_weight_units] = None,
        synthesis: Optional[Synthesis] = None,
        film_preparation: Optional[Film_preparation] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Sample' to attribute sample

        Args:
            id (str): Unique identifier of the 'Sample' object. Defaults to 'None'.
            name_product (): The name of the product.
            chemical_formula (): The chemical formula of the product. Defaults to None
            molecular_weight (): The molecular weight of the product. Defaults to None
            synthesis (): The synthesis of the product. Defaults to None
            film_preparation (): The film preparation of the product. Defaults to None
        """

        params = {
            "name_product": name_product,
            "chemical_formula": chemical_formula,
            "molecular_weight": molecular_weight,
            "synthesis": synthesis,
            "film_preparation": film_preparation,
        }

        if id is not None:
            params["id"] = id

        self.sample.append(Sample(**params))
