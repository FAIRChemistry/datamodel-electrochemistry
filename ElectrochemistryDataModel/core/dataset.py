import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .analysis import Analysis
from .purging import Purging
from .generalinformation import GeneralInformation
from .experiment_type import Experiment_type
from .electrolyte import Electrolyte
from .experiment import Experiment
from .electrodesetup import ElectrodeSetup
from .sample import Sample


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

    experiments: List[Experiment] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The experiments for work",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="dc67c22265598c1101fdc2de1850336d9dfc714f"
    )

    def add_to_experiments(
        self,
        name: Optional[str] = None,
        sample: Optional[Sample] = None,
        filename: Optional[str] = None,
        information: Optional[str] = None,
        electrode_setup: Optional[ElectrodeSetup] = None,
        electrolyte: Optional[Electrolyte] = None,
        purging: Optional[Purging] = None,
        analysis: Optional[Analysis] = None,
        type: Optional[Experiment_type] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Experiment' to attribute experiments

        Args:
            id (str): Unique identifier of the 'Experiment' object. Defaults to 'None'.
            name (): Name of the experiment. Defaults to None
            sample (): Information about the sample. Defaults to None
            filename (): Name of the experiment file (with the path). Defaults to None
            information (): Information of the experiment. Defaults to None
            electrode_setup (): Name of the used electrode materials. Defaults to None
            electrolyte (): The used electrolyte. Defaults to None
            purging (): The purging information for the experiment. Defaults to None
            analysis (): The analysis type of the experiment. Defaults to None
            type (): Type of experiment. Defaults to None
        """

        params = {
            "name": name,
            "sample": sample,
            "filename": filename,
            "information": information,
            "electrode_setup": electrode_setup,
            "electrolyte": electrolyte,
            "purging": purging,
            "analysis": analysis,
            "type": type,
        }

        if id is not None:
            params["id"] = id

        self.experiments.append(Experiment(**params))
