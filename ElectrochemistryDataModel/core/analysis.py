import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .scan_rate_units import Scan_rate_units
from .ca import CA
from .ferrocene_reference import Ferrocene_reference
from .time_units import Time_units
from .charge_density_units import Charge_density_units
from .potential_units import Potential_units
from .cp import CP
from .current_units import Current_units
from .cv import CV


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
        description="Cyclic voltammetry",
        default_factory=ListPlus,
    )

    ca: List[CA] = Field(
        multiple=True,
        description="Chronoamperometry",
        default_factory=ListPlus,
    )

    cp: List[CP] = Field(
        multiple=True,
        description="Chronopotentiometry",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="6554a2e922d0b3b07b953d3e331372ff9b7ec468"
    )

    def add_cv_to_cv(
        self,
        scan_rate: Scan_rate_units,
        start_potential: Potential_units,
        stop_potential: Potential_units,
        potential_lower_limit: Potential_units,
        potential_upper_limit: Potential_units,
        total_cycle_number: int,
        ferrocene_reference: List[Ferrocene_reference] = ListPlus(),
        halfe_wave_potential: List[Potential_units] = ListPlus(),
        i_pc_ox: List[Current_units] = ListPlus(),
        i_pa_red: List[Current_units] = ListPlus(),
        ox_potential_E_pc: List[Potential_units] = ListPlus(),
        red_potential_E_pa: List[Potential_units] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'CV' to attribute cv

        Args:
            id (str): Unique identifier of the 'CV' object. Defaults to 'None'.
            scan_rate (): The scan rate of the measurement.
            start_potential (): The starting value of the potential.
            stop_potential (): The stop value of the potential.
            potential_lower_limit (): The lower limit of the potential.
            potential_upper_limit (): The upper limit of the potential.
            total_cycle_number (): The total cycle number.
            ferrocene_reference (): Parameters of the ferocene reference measurement. Defaults to ListPlus()
            halfe_wave_potential (): The half-wave potential of the measurement. Defaults to ListPlus()
            i_pc_ox (): The current at the maximum of the cathodic peak (oxidation). Defaults to ListPlus()
            i_pa_red (): The current at the maximum of the anodic peak (reduction). Defaults to ListPlus()
            ox_potential_E_pc (): Potential at the maximum of the cathodic peak (reduction). Defaults to ListPlus()
            red_potential_E_pa (): The current at the maximum of the anodic peak (oxidation). Defaults to ListPlus()
        """

        params = {
            "scan_rate": scan_rate,
            "start_potential": start_potential,
            "stop_potential": stop_potential,
            "potential_lower_limit": potential_lower_limit,
            "potential_upper_limit": potential_upper_limit,
            "total_cycle_number": total_cycle_number,
            "ferrocene_reference": ferrocene_reference,
            "halfe_wave_potential": halfe_wave_potential,
            "i_pc_ox": i_pc_ox,
            "i_pa_red": i_pa_red,
            "ox_potential_E_pc": ox_potential_E_pc,
            "red_potential_E_pa": red_potential_E_pa,
        }

        if id is not None:
            params["id"] = id

        self.cv.append(CV(**params))

    def add_ca_to_ca(
        self,
        induced_potential_first: Potential_units,
        time_duration: Time_units,
        current_end_value: Current_units,
        induced_potential_second: Optional[Potential_units] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'CA' to attribute ca

        Args:
            id (str): Unique identifier of the 'CA' object. Defaults to 'None'.
            induced_potential_first (): The first induced potential.
            time_duration (): The duration time of the induced potential.
            current_end_value (): The current value at the end of the measurement.
            induced_potential_second (): The second induced potential. Defaults to None
        """

        params = {
            "induced_potential_first": induced_potential_first,
            "time_duration": time_duration,
            "current_end_value": current_end_value,
            "induced_potential_second": induced_potential_second,
        }

        if id is not None:
            params["id"] = id

        self.ca.append(CA(**params))

    def add_cp_to_cp(
        self,
        induced_current_first: Current_units,
        induced_current_second: Current_units,
        time_duration: Time_units,
        potential_end_value: Potential_units,
        charge_density: List[Charge_density_units] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'CP' to attribute cp

        Args:
            id (str): Unique identifier of the 'CP' object. Defaults to 'None'.
            induced_current_first (): The first induced current.
            induced_current_second (): The first induced current.
            time_duration (): The duration time of the induced current.
            potential_end_value (): The potential value at the end of the measurement.
            charge_density (): The charge density of the measurement. Defaults to ListPlus()
        """

        params = {
            "induced_current_first": induced_current_first,
            "induced_current_second": induced_current_second,
            "time_duration": time_duration,
            "potential_end_value": potential_end_value,
            "charge_density": charge_density,
        }

        if id is not None:
            params["id"] = id

        self.cp.append(CP(**params))
