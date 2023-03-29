import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .time_units import Time_units
from .elektrode_setup import Elektrode_setup
from .scan_rate_units import Scan_rate_units
from .current_units import Current_units
from .cv import CV
from .ferrocene_reference import Ferrocene_reference
from .potential_units import Potential_units
from .cp import CP
from .ca import CA


@forge_signature
class Analysis(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("analysisINDEX"),
        xml="@id",
    )

    cv: List[CV] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Cyclic voltammetry",
    )

    ca: List[CA] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Chronoamperometry",
    )

    cp: List[CP] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Chronopotentiometry",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="f7bda00987d9745b6e532491534c6fb55777ff96"
    )

    def add_cv_to_cv(
        self,
        electrode_setup: Elektrode_setup,
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
        ferrocene_reference: List[Ferrocene_reference] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'CV' to attribute cv

        Args:
            id (str): Unique identifier of the 'CV' object. Defaults to 'None'.
            electrode_setup (): Name of the used electrod materials.
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
            ferrocene_reference (): Parameters of the ferocene reference measurement. Defaults to ListPlus()
        """

        params = {
            "electrode_setup": electrode_setup,
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
            "ferrocene_reference": ferrocene_reference,
        }

        if id is not None:
            params["id"] = id

        self.cv.append(CV(**params))

    def add_ca_to_ca(
        self,
        induced_potential_first: Potential_units,
        induced_potential_second: Potential_units,
        time_duration: Time_units,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'CA' to attribute ca

        Args:
            id (str): Unique identifier of the 'CA' object. Defaults to 'None'.
            induced_potential_first (): The first induced potential.
            induced_potential_second (): The second induced potential.
            time_duration (): The duration time of the induced potential.
        """

        params = {
            "induced_potential_first": induced_potential_first,
            "induced_potential_second": induced_potential_second,
            "time_duration": time_duration,
        }

        if id is not None:
            params["id"] = id

        self.ca.append(CA(**params))

    def add_cp_to_cp(
        self,
        induced_current_first: Current_units,
        time_duration: Time_units,
        induced_current_second: Optional[Current_units] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'CP' to attribute cp

        Args:
            id (str): Unique identifier of the 'CP' object. Defaults to 'None'.
            induced_current_first (): The first induced current.
            time_duration (): The duration time of the induced current.
            induced_current_second (): The first induced current. Defaults to None
        """

        params = {
            "induced_current_first": induced_current_first,
            "time_duration": time_duration,
            "induced_current_second": induced_current_second,
        }

        if id is not None:
            params["id"] = id

        self.cp.append(CP(**params))
