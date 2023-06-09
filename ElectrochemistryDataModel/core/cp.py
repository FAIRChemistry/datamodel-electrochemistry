import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .experiment import Experiment
from .potentialunits import PotentialUnits
from .currentunits import CurrentUnits
from .experiment_type import Experiment_type
from .electrolyte import Electrolyte
from .areaunits import AreaUnits
from .timeunits import TimeUnits
from .chargedensityunits import ChargeDensityUnits
from .electrodesetup import ElectrodeSetup


@forge_signature
class CP(sdRDM.DataModel):

    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cpINDEX"),
        xml="@id",
    )

    induced_current: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The induced current",
    )

    induced_current_unit: Optional[CurrentUnits] = Field(
        default=None,
        description="The induced current",
    )

    induced_current_second: Optional[CurrentUnits] = Field(
        default=None,
        description="The first induced current",
    )

    time_duration: Optional[TimeUnits] = Field(
        default=None,
        description="The duration time of the induced current",
    )

    potential_end_value: Optional[PotentialUnits] = Field(
        default=None,
        description="The potential value at the end of the measurement",
    )

    charge_density: List[ChargeDensityUnits] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The charge density of the measurement",
    )

    cp_experiments: List[Experiment] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="experiments",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="104c20baf27e49c578eb70468cffff3483cad6f0"
    )

    def add_to_cp_experiments(
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
        This method adds an object of type 'Experiment' to attribute cp_experiments

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

        self.cp_experiments.append(Experiment(**params))
