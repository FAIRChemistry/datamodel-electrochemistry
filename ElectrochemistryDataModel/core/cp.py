import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .potentialendvalue import PotentialEndValue
from .timeunits import TimeUnits
from .chargedensityunits import ChargeDensityUnits
from .potentialunits import PotentialUnits
from .currentunits import CurrentUnits


@forge_signature
class CP(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cpINDEX"),
        xml="@id",
    )

    measurement_potential_unit: Optional[PotentialUnits] = Field(
        default=None,
        description="The potential unit of the measurement",
    )

    measurement_time_unit: Optional[TimeUnits] = Field(
        default=None,
        description="The time unit of the measurement",
    )

    induced_current: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The induced current",
    )

    induced_current_unit: Optional[CurrentUnits] = Field(
        default=None,
        description="The induced current unit",
    )

    time_duration: Optional[float] = Field(
        default=None,
        description="The duration time of the induced current",
    )

    time_duration_unit: Optional[TimeUnits] = Field(
        default=None,
        description="The duration time unit of the induced current",
    )

    potential_end_value: List[PotentialEndValue] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The potential value at the end of the measurement",
    )

    charge_density: List[ChargeDensityUnits] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The charge density of the measurement",
    )

    change_potential: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "A list of potential values, which could be used to transform reference"
            " potential scale"
        ),
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="ba6aa04635d73779d00c7c6b39e863c4ba93ef80"
    )

    def add_to_potential_end_value(
        self,
        method: Optional[str] = None,
        end_value: Optional[float] = None,
        reference_name: Optional[str] = None,
        change_reference_potential: Optional[float] = None,
        last_average_points: Optional[int] = None,
        fit_function: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'PotentialEndValue' to attribute potential_end_value

        Args:
            id (str): Unique identifier of the 'PotentialEndValue' object. Defaults to 'None'.
            method (): The method, which was used to determine this value. Defaults to None
            end_value (): The end value potential. Defaults to None
            reference_name (): The used reference scale. Defaults to None
            change_reference_potential (): The change_reference potential. Defaults to None
            last_average_points (): The last points, which were used to calculate the average. Defaults to None
            fit_function (): The fit function, if the fit function was used. Defaults to None
        """

        params = {
            "method": method,
            "end_value": end_value,
            "reference_name": reference_name,
            "change_reference_potential": change_reference_potential,
            "last_average_points": last_average_points,
            "fit_function": fit_function,
        }

        if id is not None:
            params["id"] = id

        self.potential_end_value.append(PotentialEndValue(**params))
