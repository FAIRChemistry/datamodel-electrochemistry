import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .peakintegration import PeakIntegration
from .currentunits import CurrentUnits
from .peaksandhalfpotential import PeaksAndHalfPotential
from .cycle import Cycle
from .potentialunits import PotentialUnits
from .scanrateunits import ScanRateUnits


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

    change_potential: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "A tuple list of potential values, which could be used to transform"
            " reference potential scale"
        ),
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
        default="a1c6eab16e0b0b7e3ab6aa62c9f1d897ddab5d5f"
    )

    def add_to_cycles(
        self,
        number: Optional[int] = None,
        scan_rate: Optional[float] = None,
        scan_rate_unit: Optional[ScanRateUnits] = None,
        current_vertex: Optional[float] = None,
        y_unit_vertex: Optional[str] = None,
        change_reference_potential: Optional[float] = None,
        reference_name: Optional[str] = None,
        potential_vertex: Optional[float] = None,
        peaks_and_half_potential: List[PeaksAndHalfPotential] = ListPlus(),
        peak_integration: List[PeakIntegration] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Cycle' to attribute cycles

        Args:
            id (str): Unique identifier of the 'Cycle' object. Defaults to 'None'.
            number (): The cycle number. Defaults to None
            scan_rate (): The scan rate of the measurement. Defaults to None
            scan_rate_unit (): The scan rate unit of the measurement. Defaults to None
            current_vertex (): The vertex current. Defaults to None
            y_unit_vertex (): The y unit. Defaults to None
            change_reference_potential (): The change_reference potential. Defaults to None
            reference_name (): The used reference scale. Defaults to None
            potential_vertex (): The vertex potential. Defaults to None
            peaks_and_half_potential (): The half-wave potential of the measurement. Defaults to ListPlus()
            peak_integration (): The peak integration. Defaults to ListPlus()
        """

        params = {
            "number": number,
            "scan_rate": scan_rate,
            "scan_rate_unit": scan_rate_unit,
            "current_vertex": current_vertex,
            "y_unit_vertex": y_unit_vertex,
            "change_reference_potential": change_reference_potential,
            "reference_name": reference_name,
            "potential_vertex": potential_vertex,
            "peaks_and_half_potential": peaks_and_half_potential,
            "peak_integration": peak_integration,
        }

        if id is not None:
            params["id"] = id

        self.cycles.append(Cycle(**params))
