import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .potentialunits import PotentialUnits
from .ferrocene_reference import Ferrocene_reference
from .scanrateunits import ScanRateUnits
from .currentunits import CurrentUnits


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

    halfe_wave_potential: List[PotentialUnits] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The half-wave potential of the measurement",
    )

    scan_rate: Optional[ScanRateUnits] = Field(
        default=None,
        description="The scan rate of the measurement",
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

    i_pc_ox: List[CurrentUnits] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The current at the maximum of the cathodic peak (oxidation)",
    )

    i_pa_red: List[CurrentUnits] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The current at the maximum of the anodic peak (reduction)",
    )

    ox_potential_E_pc: List[PotentialUnits] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Potential at the maximum of the cathodic peak (reduction)",
    )

    red_potential_E_pa: List[PotentialUnits] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The current at the maximum of the anodic peak (oxidation)",
    )

    total_cycle_number: Optional[int] = Field(
        default=None,
        description="The total cycle number",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c6be0fb60bd88decea3c28b088cb701ff65e7dda"
    )

    def add_to_ferrocene_reference(
        self,
        ox_potential_E_pc_ferrocene: Optional[PotentialUnits] = None,
        red_potential_E_pa_ferrocene: Optional[PotentialUnits] = None,
        halfe_wave_potential_ferrocene: Optional[PotentialUnits] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Ferrocene_reference' to attribute ferrocene_reference

        Args:
            id (str): Unique identifier of the 'Ferrocene_reference' object. Defaults to 'None'.
            ox_potential_E_pc_ferrocene (): Potential at the maximum of the cathodic peak (reduction) of the ferrocene reference. Defaults to None
            red_potential_E_pa_ferrocene (): The current at the maximum of the anodic peak (oxidation) of the ferrocene reference. Defaults to None
            halfe_wave_potential_ferrocene (): The half-wave potential of the ferrocene measurement. Defaults to None
        """

        params = {
            "ox_potential_E_pc_ferrocene": ox_potential_E_pc_ferrocene,
            "red_potential_E_pa_ferrocene": red_potential_E_pa_ferrocene,
            "halfe_wave_potential_ferrocene": halfe_wave_potential_ferrocene,
        }

        if id is not None:
            params["id"] = id

        self.ferrocene_reference.append(Ferrocene_reference(**params))
