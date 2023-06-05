import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .experiment_type import Experiment_type
from .timeunits import TimeUnits
from .potentialunits import PotentialUnits
from .experiment import Experiment
from .areaunits import AreaUnits
from .electrodesetup import ElectrodeSetup
from .currentunits import CurrentUnits


@forge_signature
class CA(sdRDM.DataModel):

    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("caINDEX"),
        xml="@id",
    )

    induced_potential_first: Optional[PotentialUnits] = Field(
        default=None,
        description="The first induced potential",
    )

    induced_potential_second: Optional[PotentialUnits] = Field(
        default=None,
        description="The second induced potential",
    )

    time_duration: Optional[TimeUnits] = Field(
        default=None,
        description="The duration time of the induced potential",
    )

    current_end_value: Optional[CurrentUnits] = Field(
        default=None,
        description="The current value at the end of the measurement",
    )

    ca_experiments: List[Experiment] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="experiments",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="335acb05751730a5198440bdad0c7b9bb4896787"
    )

    def add_to_ca_experiments(
        self,
        name: Optional[str] = None,
        filename: Optional[str] = None,
        WE_material: Optional[str] = None,
        WE_area: Optional[AreaUnits] = None,
        solvent_test: Optional[str] = None,
        electrode_setup_test: Optional[ElectrodeSetup] = None,
        type: Optional[Experiment_type] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Experiment' to attribute ca_experiments

        Args:
            id (str): Unique identifier of the 'Experiment' object. Defaults to 'None'.
            name (): Name of the experiment. Defaults to None
            filename (): Name of the experiment file (with the path). Defaults to None
            WE_material (): Name of the used working electrode material. Defaults to None
            WE_area (): The area of the used working electrode. Defaults to None
            solvent_test (): Name of the solvent. Defaults to None
            electrode_setup_test (): Name of the used electrode materials. Defaults to None
            type (): Type of experiment. Defaults to None
        """

        params = {
            "name": name,
            "filename": filename,
            "WE_material": WE_material,
            "WE_area": WE_area,
            "solvent_test": solvent_test,
            "electrode_setup_test": electrode_setup_test,
            "type": type,
        }

        if id is not None:
            params["id"] = id

        self.ca_experiments.append(Experiment(**params))
