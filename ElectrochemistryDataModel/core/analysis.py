import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .concentration_units import Concentration_units
from .cp import CP
from .scan_rate_units import Scan_rate_units
from .potential_units import Potential_units
from .cv import CV
from .current_units import Current_units
from .time_units import Time_units


@forge_signature
class Analysis(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("analysisINDEX"),
        xml="@id",
    )

    cv: List[CV] = Field(
        multiple=True,
        description="Cyclic Voltammetry",
        default_factory=ListPlus,
    )

    cp: List[CP] = Field(
        multiple=True,
        description="Chronoamperometry",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="32d178071e5fb3a810cab716ec136f2683546f94"
    )

    def add_cv_to_cv(
        self,
        electrode_material: str,
        solvent: str,
        conducting_salt: str,
        conducting_salt_concentration: Concentration_units,
        halfe_wave_potential: Potential_units,
        scan_rate: Scan_rate_units,
        start_potential: Potential_units,
        stop_potential: Potential_units,
        potential_lower_limit: Potential_units,
        potential_upper_limit: Potential_units,
        i_pc_ox: Current_units,
        i_pa_red: Current_units,
        ox_potential_E_pc: Potential_units,
        red_potential_E_pa: Potential_units,
        total_cycle_number: int,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'CV' to attribute cv

        Args:
            id (str): Unique identifier of the 'CV' object. Defaults to 'None'.
            electrode_material (): Name of the used electrode material.
            solvent (): Name of the solvent.
            conducting_salt (): Name of the used salt.
            conducting_salt_concentration (): Concentration of the conducting salt.
            halfe_wave_potential (): The half-wave potential of the measurement.
            scan_rate (): The scan rate of the measurement.
            start_potential (): The starting value of the potential.
            stop_potential (): The stop value of the potential.
            potential_lower_limit (): The lower limit of the potential.
            potential_upper_limit (): The upper limit of the potential.
            i_pc_ox (): The current at the maximum of the cathodic peak (oxidation).
            i_pa_red (): The current at the maximum of the anodic peak (reduction).
            ox_potential_E_pc (): Potential at the maximum of the cathodic peak (reduction).
            red_potential_E_pa (): The current at the maximum of the anodic peak (oxidation).
            total_cycle_number (): The total cycle number.
        """

        params = {
            "electrode_material": electrode_material,
            "solvent": solvent,
            "conducting_salt": conducting_salt,
            "conducting_salt_concentration": conducting_salt_concentration,
            "halfe_wave_potential": halfe_wave_potential,
            "scan_rate": scan_rate,
            "start_potential": start_potential,
            "stop_potential": stop_potential,
            "potential_lower_limit": potential_lower_limit,
            "potential_upper_limit": potential_upper_limit,
            "i_pc_ox": i_pc_ox,
            "i_pa_red": i_pa_red,
            "ox_potential_E_pc": ox_potential_E_pc,
            "red_potential_E_pa": red_potential_E_pa,
            "total_cycle_number": total_cycle_number,
        }

        if id is not None:
            params["id"] = id

        self.cv.append(CV(**params))

    def add_cp_to_cp(
        self,
        electrode_material: str,
        solvent: str,
        conducting_salt: str,
        conducting_salt_concentration: Concentration_units,
        potential_first: Potential_units,
        potential_second: Potential_units,
        time_duration: Time_units,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'CP' to attribute cp

        Args:
            id (str): Unique identifier of the 'CP' object. Defaults to 'None'.
            electrode_material (): Name of the used electrode material.
            solvent (): Name of the solvent.
            conducting_salt (): Name of the used salt.
            conducting_salt_concentration (): Concentration of the conducting salt.
            potential_first (): The first induced potential.
            potential_second (): The second induced potential.
            time_duration (): The time duration of the potential.
        """

        params = {
            "electrode_material": electrode_material,
            "solvent": solvent,
            "conducting_salt": conducting_salt,
            "conducting_salt_concentration": conducting_salt_concentration,
            "potential_first": potential_first,
            "potential_second": potential_second,
            "time_duration": time_duration,
        }

        if id is not None:
            params["id"] = id

        self.cp.append(CP(**params))
