import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .concentrationunits import ConcentrationUnits
from .filmpreparation import FilmPreparation
from .electrodesetup import ElectrodeSetup
from .areaunits import AreaUnits
from .sample import Sample
from .analysis import Analysis
from .molecularweightunits import MolecularWeightUnits
from .generalinformation import GeneralInformation
from .synthesis import Synthesis
from .experiment import Experiment


@forge_signature
class Dataset(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("datasetINDEX"),
        xml="@id",
    )

    general_information: Optional[GeneralInformation] = Field(
        default=None,
        description="General information about the data model",
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

    conducting_salt_concentration: Optional[ConcentrationUnits] = Field(
        default=None,
        description="Concentration of the conducting salt",
    )

    electrode_setup: Optional[ElectrodeSetup] = Field(
        default=None,
        description="Name of the used electrode materials",
    )

    experiments: List[Experiment] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The experiments of the work",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="467f3e8f6d8b1de1aae94e39025cbac80bda24b9"
    )

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

    def add_to_experiments(
        self,
        experiment_name: Optional[str] = None,
        experiment_filename: Optional[str] = None,
        WE_material: Optional[str] = None,
        WE_area: Optional[AreaUnits] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Experiment' to attribute experiments

        Args:
            id (str): Unique identifier of the 'Experiment' object. Defaults to 'None'.
            experiment_name (): Name of the experiment. Defaults to None
            experiment_filename (): Name of the experiment file (with the path). Defaults to None
            WE_material (): Name of the used working electrode material. Defaults to None
            WE_area (): The area of the used working electrode. Defaults to None
        """

        params = {
            "experiment_name": experiment_name,
            "experiment_filename": experiment_filename,
            "WE_material": WE_material,
            "WE_area": WE_area,
        }

        if id is not None:
            params["id"] = id

        self.experiments.append(Experiment(**params))
