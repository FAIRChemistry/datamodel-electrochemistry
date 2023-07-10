import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .currentunits import CurrentUnits
from .scanrateunits import ScanRateUnits
from .potentialunits import PotentialUnits
from .cycle import Cycle


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

    cycles: Optional[Cycle] = Field(
        default=None,
        description="The cycles",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="65794cd39ea7a9558c9962ff1fa4049d3a3e581d"
    )
