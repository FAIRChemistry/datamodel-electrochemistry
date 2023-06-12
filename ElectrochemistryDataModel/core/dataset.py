import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .experiment_type import Experiment_type
from .experiment import Experiment
from .generalinformation import GeneralInformation
from .electrolyte import Electrolyte
from .electrodesetup import ElectrodeSetup
from .analysis import Analysis
from .areaunits import AreaUnits
from .concentrationunits import ConcentrationUnits


@forge_signature
class Dataset(sdRDM.DataModel):

    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("datasetINDEX"),
        xml="@id",
    )

    general_information: Optional[GeneralInformation] = Field(
        default=None,
        description="General information about the data model",
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

    conducting_salt_concentration: Optional[float] = Field(
        default=None,
        description="Concentration of the conducting salt",
    )

    conducting_salt_concentration_unit: Optional[ConcentrationUnits] = Field(
        default=None,
        description="Unit of the conducting salt concentration",
    )

    experiments: List[Experiment] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The experiments for work",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="122b947ee62a907093952580635d1c9eea3881a6"
    )

    def add_to_experiments(
        self,
        name: Optional[str] = None,
        filename: Optional[str] = None,
        WE_material: Optional[str] = None,
        WE_area: Optional[AreaUnits] = None,
        solvent_test: Optional[str] = None,
        electrode_setup: Optional[ElectrodeSetup] = None,
        electrolyte: Optional[Electrolyte] = None,
        type: Optional[Experiment_type] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Experiment' to attribute experiments

        Args:
            id (str): Unique identifier of the 'Experiment' object. Defaults to 'None'.
            name (): Name of the experiment. Defaults to None
            filename (): Name of the experiment file (with the path). Defaults to None
            WE_material (): Name of the used working electrode material. Defaults to None
            WE_area (): The area of the used working electrode. Defaults to None
            solvent_test (): Name of the solvent. Defaults to None
            electrode_setup (): Name of the used electrode materials. Defaults to None
            electrolyte (): The used electrolyte. Defaults to None
            type (): Type of experiment. Defaults to None
        """

        params = {
            "name": name,
            "filename": filename,
            "WE_material": WE_material,
            "WE_area": WE_area,
            "solvent_test": solvent_test,
            "electrode_setup": electrode_setup,
            "electrolyte": electrolyte,
            "type": type,
        }

        if id is not None:
            params["id"] = id

        self.experiments.append(Experiment(**params))
