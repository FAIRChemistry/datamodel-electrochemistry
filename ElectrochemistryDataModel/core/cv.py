import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .cycle import Cycle
from .scanrateunits import ScanRateUnits
from .currentunits import CurrentUnits
from .potentialunits import PotentialUnits


@forge_signature
class CV(sdRDM.DataModel):
    """Container for information regarding the CV-Setup and parameters"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cvINDEX"),
        xml="@id",
    )

    changing_potential: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The potential which should be added",
    )

    changing_potential_unit: Optional[float] = Field(
        default=None,
        description="The unit of the added potential",
    )

    ferrocene_potential: Optional[float] = Field(
        default=None,
        description="ferrocene_potential",
    )

    measurement_current_unit: Optional[CurrentUnits] = Field(
        default=None,
        description="The current unit of the measurement",
    )

    measurement_potential_unit: Optional[PotentialUnits] = Field(
        default=None,
        description="The unit of the Potential",
    )

    scan_rate: Optional[float] = Field(
        default=None,
        description="The scan rate of the measurement",
    )

    scan_rate_unit: Optional[ScanRateUnits] = Field(
        default=None,
        description="The scan rate unit of the measurement",
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

    cycles: List[Cycle] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The cycles",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="5abdf055175ec1845bee4fce936bab8038dd6f5f"
    )

    def add_to_cycles(
        self,
        cycle_number: List[str] = ListPlus(),
        peak_maxima: List[float] = ListPlus(),
        peak_minima: List[float] = ListPlus(),
        half_wave_potential: List[float] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Cycle' to attribute cycles

        Args:
            id (str): Unique identifier of the 'Cycle' object. Defaults to 'None'.
            cycle_number (): A list of the cycles. Defaults to ListPlus()
            peak_maxima (): A list of the peak maxima. Defaults to ListPlus()
            peak_minima (): A list of the peak minima. Defaults to ListPlus()
            half_wave_potential (): The half-wave potential of the measurement. Defaults to ListPlus()
        """

        params = {
            "cycle_number": cycle_number,
            "peak_maxima": peak_maxima,
            "peak_minima": peak_minima,
            "half_wave_potential": half_wave_potential,
        }

        if id is not None:
            params["id"] = id

        self.cycles.append(Cycle(**params))
