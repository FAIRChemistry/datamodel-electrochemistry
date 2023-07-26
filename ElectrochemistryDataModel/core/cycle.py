import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


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

    peak_maxima: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="A list of the peak maxima",
    )

    peak_minima: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="A list of the peak minima",
    )

    half_wave_potential: List[float] = Field(
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
        default="ce235b09a292fbf86d3ec367d054958dbe6889e1"
    )

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
