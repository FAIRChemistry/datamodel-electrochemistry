import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .cv import CV
from .concentration_units import Concentration_units
from .time_units import Time_units
from .potential_units import Potential_units
from .scan_rate_units import Scan_rate_units
from .current_units import Current_units
from .cp import CP


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
        description="cv",
        default_factory=ListPlus,
    )

    cp: List[CP] = Field(
        multiple=True,
        description="cp",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="723b7621cb273f11a5d3bf188d93df0af6426495"
    )

    def add_cv_to_cv(
        self,
        solvent: str,
        conducting_salt: str,
        conducting_salt_concentration: Concentration_units,
        halfe_wave_potential: Potential_units,
        scan_rate: Scan_rate_units,
        start_potential: Potential_units,
        stop_potential: Potential_units,
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
            solvent (): Name of the solvent.
            conducting_salt (): Name of the used salt.
            conducting_salt_concentration (): Concentration of the conducting salt.
            halfe_wave_potential (): The half-wave potential of the measurement.
            scan_rate (): The scan rate of the measurement.
            start_potential (): The starting value of the potential.
            stop_potential (): The stop value of the potential.
            i_pc_ox (): The current at the maximum of the cathodic peak (oxidation).
            i_pa_red (): The current at the maximum of the anodic peak (reduction).
            ox_potential_E_pc (): Potential at the maximum of the cathodic peak (reduction).
            red_potential_E_pa (): The current at the maximum of the anodic peak (oxidation).
            total_cycle_number (): The total cycle number.
        """

        params = {
            "solvent": solvent,
            "conducting_salt": conducting_salt,
            "conducting_salt_concentration": conducting_salt_concentration,
            "halfe_wave_potential": halfe_wave_potential,
            "scan_rate": scan_rate,
            "start_potential": start_potential,
            "stop_potential": stop_potential,
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
        solvent: str,
        conducting_salt: str,
        conducting_salt_concentration: Concentration_units,
        potential_first: Potential_units,
        potential_sec: Potential_units,
        time_between_switch: Time_units,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'CP' to attribute cp

        Args:
            id (str): Unique identifier of the 'CP' object. Defaults to 'None'.
            solvent (): Name of the solvent.
            conducting_salt (): Name of the used salt.
            conducting_salt_concentration (): Concentration of the conducting salt.
            potential_first (): First potential which was used.
            potential_sec (): Second potential which was used.
            time_between_switch (): The time between switching the potentials.
        """

        params = {
            "solvent": solvent,
            "conducting_salt": conducting_salt,
            "conducting_salt_concentration": conducting_salt_concentration,
            "potential_first": potential_first,
            "potential_sec": potential_sec,
            "time_between_switch": time_between_switch,
        }

        if id is not None:
            params["id"] = id

        self.cp.append(CP(**params))
