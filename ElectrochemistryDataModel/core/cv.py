import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .concentration_units import Concentration_units
from .scan_rate_units import Scan_rate_units
from .potential_units import Potential_units
from .current_units import Current_units


@forge_signature
class CV(sdRDM.DataModel):

    """Container for information regarding the CV-Setup and parameters"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cvINDEX"),
        xml="@id",
    )

    electrode_material: str = Field(
        ...,
        description="Name of the used electrode material",
    )

    solvent: str = Field(
        ...,
        description="Name of the solvent",
    )

    conducting_salt: str = Field(
        ...,
        description="Name of the used salt",
    )

    conducting_salt_concentration: Concentration_units = Field(
        ...,
        description="Concentration of the conducting salt",
    )

    halfe_wave_potential: Potential_units = Field(
        ...,
        description="The half-wave potential of the measurement",
    )

    scan_rate: Scan_rate_units = Field(
        ...,
        description="The scan rate of the measurement",
    )

    start_potential: Potential_units = Field(
        ...,
        description="The starting value of the potential",
    )

    stop_potential: Potential_units = Field(
        ...,
        description="The stop value of the potential",
    )

    potential_lower_limit: Potential_units = Field(
        ...,
        description="The lower limit of the potential",
    )

    potential_upper_limit: Potential_units = Field(
        ...,
        description="The upper limit of the potential",
    )

    i_pc_ox: Current_units = Field(
        ...,
        description="The current at the maximum of the cathodic peak (oxidation)",
    )

    i_pa_red: Current_units = Field(
        ...,
        description="The current at the maximum of the anodic peak (reduction)",
    )

    ox_potential_E_pc: Potential_units = Field(
        ...,
        description="Potential at the maximum of the cathodic peak (reduction)",
    )

    red_potential_E_pa: Potential_units = Field(
        ...,
        description="The current at the maximum of the anodic peak (oxidation)",
    )

    total_cycle_number: int = Field(
        ...,
        description="The total cycle number",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="32d178071e5fb3a810cab716ec136f2683546f94"
    )
