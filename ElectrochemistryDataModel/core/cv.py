import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .currentunits import CurrentUnits
from .experiment import Experiment
from .potentialunits import PotentialUnits
from .scanrateunits import ScanRateUnits
from .experiment_type import Experiment_type
from .areaunits import AreaUnits


@forge_signature
class CV(sdRDM.DataModel):

    """Container for information regarding the CV-Setup and parameters"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cvINDEX"),
        xml="@id",
    )

    cp_experiments: List[Experiment] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="experiments",
    )

    half_wave_potential: List[PotentialUnits] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The half-wave potential of the measurement",
    )

    scan_rate: Optional[ScanRateUnits] = Field(
        default=None,
        description="The scan rate of the measurement",
    )

    start_potential: Optional[PotentialUnits] = Field(
        default=None,
        description="The starting value of the potential",
    )

    stop_potential: Optional[PotentialUnits] = Field(
        default=None,
        description="The stop value of the potential",
    )

    potential_lower_limit: Optional[PotentialUnits] = Field(
        default=None,
        description="The lower limit of the potential",
    )

    potential_upper_limit: Optional[PotentialUnits] = Field(
        default=None,
        description="The upper limit of the potential",
    )

    i_pc_ox: List[CurrentUnits] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The current at the maximum of the cathodic peak (oxidation)",
    )

    i_pa_red: List[CurrentUnits] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The current at the maximum of the anodic peak (reduction)",
    )

    ox_potential_E_pc: List[PotentialUnits] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Potential at the maximum of the cathodic peak (reduction)",
    )

    red_potential_E_pa: List[PotentialUnits] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The current at the maximum of the anodic peak (oxidation)",
    )

    total_cycle_number: Optional[int] = Field(
        default=None,
        description="The total cycle number",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="5622c5ebe8090880fbfb344d4ee1d3274c05b99a"
    )

    def add_to_cp_experiments(
        self,
        name: Optional[str] = None,
        filename: Optional[str] = None,
        WE_material: Optional[str] = None,
        WE_area: Optional[AreaUnits] = None,
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
            type (): Type of experiment. Defaults to None
        """

        params = {
            "name": name,
            "filename": filename,
            "WE_material": WE_material,
            "WE_area": WE_area,
            "type": type,
        }

        if id is not None:
            params["id"] = id

        self.cp_experiments.append(Experiment(**params))
