import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic.types import Enum
from datetime import date

from .synthesis import Synthesis
from .author import Author
from .molecularweightunits import MolecularWeightUnits
from .electrodesetup import ElectrodeSetup
from .sample import Sample
from .filmpreparation import FilmPreparation
from .analysis import Analysis


@forge_signature
class Dataset(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("datasetINDEX"),
        xml="@id",
    )

    name: Optional[str] = Field(
        default=None,
        description="Name of the dataset",
    )

    date_created: Optional[date] = Field(
        default=None,
        description="Date/time when the dataset was created",
    )

    author: List[Author] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Persons who worked on the dataset",
    )

    sample: List[Sample] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The sample which was measured",
    )

    analysis: Optional[Analysis] = Field(
        default=None,
        description="The method which is used to gain the data",
    )

    solvent: Optional[str] = Field(
        default=None,
        description="Name of the solvent",
    )

    conducting_salt: Optional[str] = Field(
        default=None,
        description="Name of the used salt",
    )

    conducting_salt_concentration: Optional[Enum] = Field(
        default=None,
        description="Concentration of the conducting salt",
    )

    electrode_setup: Optional[ElectrodeSetup] = Field(
        default=None,
        description="Name of the used electrode materials",
    )

    experiment: List[str] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Name of the experiment files",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="fc48575810062af644232dd60f4d6117a07fb923"
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

    def add_to_sample(
        self,
        name_product: Optional[str] = None,
        chemical_formula: Optional[str] = None,
        molecular_weight: Optional[MolecularWeightUnits] = None,
        synthesis: Optional[Synthesis] = None,
        film_preparation: Optional[FilmPreparation] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Sample' to attribute sample

        Args:
            id (str): Unique identifier of the 'Sample' object. Defaults to 'None'.
            name_product (): The name of the product. Defaults to None
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
