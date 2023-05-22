import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .currentunits import CurrentUnits
from .timeunits import TimeUnits
from .areaunits import AreaUnits
from .potentialunits import PotentialUnits
from .experiment import Experiment
from .chargedensityunits import ChargeDensityUnits


@forge_signature
class CP(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cpINDEX"),
        xml="@id",
    )

    induced_current_first: Optional[CurrentUnits] = Field(
        default=None,
        description="The first induced current",
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
        default="467f3e8f6d8b1de1aae94e39025cbac80bda24b9"
    )

    def add_to_cp_experiments(
        self,
        experiment_name: Optional[str] = None,
        experiment_filename: Optional[str] = None,
        WE_material: Optional[str] = None,
        WE_area: Optional[AreaUnits] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Experiment' to attribute cp_experiments

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

        self.cp_experiments.append(Experiment(**params))
