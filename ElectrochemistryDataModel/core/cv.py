import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .ferrocene_reference import Ferrocene_reference
from .current_units import Current_units
from .scan_rate_units import Scan_rate_units
from .potential_units import Potential_units


@forge_signature
class CV(sdRDM.DataModel):

    """Container for information regarding the CV-Setup and parameters"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cvINDEX"),
        xml="@id",
    )

    ferrocene_reference: List[Ferrocene_reference] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Parameters of the ferocene reference measurement",
    )

    halfe_wave_potential: List[Potential_units] = Field(
        default_factory=ListPlus,
        multiple=True,
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

    i_pc_ox: List[Current_units] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The current at the maximum of the cathodic peak (oxidation)",
    )

    i_pa_red: List[Current_units] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The current at the maximum of the anodic peak (reduction)",
    )

    ox_potential_E_pc: List[Potential_units] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Potential at the maximum of the cathodic peak (reduction)",
    )

    red_potential_E_pa: List[Potential_units] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The current at the maximum of the anodic peak (oxidation)",
    )

    total_cycle_number: Optional[int] = Field(
        default=None,
        description="The total cycle number",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="480ec8ed2f5f9ef7130c63306c48e9ded43e9f46"
    )

    def add_ferrocene_reference_to_ferrocene_reference(
        self,
        ox_potential_E_pc_ferrocene: Potential_units,
        red_potential_E_pa_ferrocene: Potential_units,
        halfe_wave_potential_ferrocene: Potential_units,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Ferrocene_reference' to attribute ferrocene_reference

        Args:
            id (str): Unique identifier of the 'Ferrocene_reference' object. Defaults to 'None'.
            ox_potential_E_pc_ferrocene (): Potential at the maximum of the cathodic peak (reduction) of the ferrocene reference.
            red_potential_E_pa_ferrocene (): The current at the maximum of the anodic peak (oxidation) of the ferrocene reference.
            halfe_wave_potential_ferrocene (): The half-wave potential of the ferrocene measurement.
        """

        params = {
            "ox_potential_E_pc_ferrocene": ox_potential_E_pc_ferrocene,
            "red_potential_E_pa_ferrocene": red_potential_E_pa_ferrocene,
            "halfe_wave_potential_ferrocene": halfe_wave_potential_ferrocene,
        }

        if id is not None:
            params["id"] = id

        self.ferrocene_reference.append(Ferrocene_reference(**params))
