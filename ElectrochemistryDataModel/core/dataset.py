import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .electrolyte import Electrolyte
from .electrodesetup import ElectrodeSetup
from .generalinformation import GeneralInformation
from .analysis import Analysis
from .sample import Sample
from .purging import Purging
from .experiment_type import Experiment_type
from .experiment import Experiment


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
        default="218c9738dc7ae356e41b06d1d73bb5dba913f6ce"
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
        date_of_work: Optional[str] = None,
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
            date_of_work (): Date/time when the experiment was created. Defaults to None
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
            "date_of_work": date_of_work,
        }

        if id is not None:
            params["id"] = id

        self.experiments.append(Experiment(**params))
