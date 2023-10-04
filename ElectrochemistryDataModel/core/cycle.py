import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .scanrateunits import ScanRateUnits
from .peaksandhalfpotential import PeaksAndHalfPotential
from .peakintegration import PeakIntegration


@forge_signature
class Cycle(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cycleINDEX"),
        xml="@id",
    )

    number: Optional[int] = Field(
        default=None,
        description="The cycle number",
    )

    scan_rate: Optional[float] = Field(
        default=None,
        description="The scan rate of the measurement",
    )

    scan_rate_unit: Optional[ScanRateUnits] = Field(
        default=None,
        description="The scan rate unit of the measurement",
    )

    current_vertex: Optional[float] = Field(
        default=None,
        description="The vertex current",
    )

    y_unit_vertex: Optional[str] = Field(
        default=None,
        description="The y unit",
    )

    change_reference_potential: Optional[float] = Field(
        default=None,
        description="The change_reference potential",
    )

    reference_name: Optional[str] = Field(
        default=None,
        description="The used reference scale",
    )

    potential_vertex: Optional[float] = Field(
        default=None,
        description="The vertex potential",
    )

    peaks_and_half_potential: List[PeaksAndHalfPotential] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The half-wave potential of the measurement",
    )

    peak_integration: List[PeakIntegration] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The peak integration",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="ddb33876bfe0e592851dc7c84d0ad9f3f5b28ec6"
    )

    def add_to_peaks_and_half_potential(
        self,
        current_maximum: Optional[float] = None,
        current_minimum: Optional[float] = None,
        potential_maximum: Optional[float] = None,
        potential_minimum: Optional[float] = None,
        y_unit: Optional[str] = None,
        change_reference_potential: Optional[float] = None,
        reference_name: Optional[str] = None,
        half_wave_potential: Optional[float] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'PeaksAndHalfPotential' to attribute peaks_and_half_potential

        Args:
            id (str): Unique identifier of the 'PeaksAndHalfPotential' object. Defaults to 'None'.
            current_maximum (): A list of the peak maxima. Defaults to None
            current_minimum (): A list of the peak minima. Defaults to None
            potential_maximum (): A list of the peak maxima. Defaults to None
            potential_minimum (): A list of the peak minima. Defaults to None
            y_unit (): The y unit. Defaults to None
            change_reference_potential (): The change_reference potential. Defaults to None
            reference_name (): The used reference scale. Defaults to None
            half_wave_potential (): The half-wave potential of the measurement. Defaults to None
        """

        params = {
            "current_maximum": current_maximum,
            "current_minimum": current_minimum,
            "potential_maximum": potential_maximum,
            "potential_minimum": potential_minimum,
            "y_unit": y_unit,
            "change_reference_potential": change_reference_potential,
            "reference_name": reference_name,
            "half_wave_potential": half_wave_potential,
        }

        if id is not None:
            params["id"] = id

        self.peaks_and_half_potential.append(PeaksAndHalfPotential(**params))

    def add_to_peak_integration(
        self,
        lower_limit_potential: Optional[float] = None,
        upper_limit_potential: Optional[float] = None,
        integration_area: Optional[float] = None,
        integration_area_unit: Optional[str] = None,
        integration_direction: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'PeakIntegration' to attribute peak_integration

        Args:
            id (str): Unique identifier of the 'PeakIntegration' object. Defaults to 'None'.
            lower_limit_potential (): Name of the used working electrode. Defaults to None
            upper_limit_potential (): Name of the used working electrode. Defaults to None
            integration_area (): Name of the used working electrode. Defaults to None
            integration_area_unit (): Name of the used working electrode. Defaults to None
            integration_direction (): The integration direction.. Defaults to None
        """

        params = {
            "lower_limit_potential": lower_limit_potential,
            "upper_limit_potential": upper_limit_potential,
            "integration_area": integration_area,
            "integration_area_unit": integration_area_unit,
            "integration_direction": integration_direction,
        }

        if id is not None:
            params["id"] = id

        self.peak_integration.append(PeakIntegration(**params))
