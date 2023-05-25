import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .timeunits import TimeUnits
from .experiment import Experiment
from .currentunits import CurrentUnits
from .potentialunits import PotentialUnits
from .areaunits import AreaUnits


@forge_signature
class CA(sdRDM.DataModel):

    """"""

    id: str = Field(
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
        default="8867c2a3e77fe6c21d29d56abe5a449b7d1454cb"
    )

    def add_to_ca_experiments(
        self,
        experiment_name: Optional[str] = None,
        experiment_filename: Optional[str] = None,
        WE_material: Optional[str] = None,
        WE_area: Optional[AreaUnits] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Experiment' to attribute ca_experiments

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

        self.ca_experiments.append(Experiment(**params))
