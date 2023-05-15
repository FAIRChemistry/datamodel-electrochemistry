import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .cv import CV
from .timeunits import TimeUnits
from .cp import CP
from .potentialunits import PotentialUnits
from .ferrocene_reference import Ferrocene_reference
from .ca import CA
from .scanrateunits import ScanRateUnits
from .chargedensityunits import ChargeDensityUnits
from .currentunits import CurrentUnits


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
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="c6be0fb60bd88decea3c28b088cb701ff65e7dda"
    )

    def add_to_cv(
        self,
        ferrocene_reference: List[Ferrocene_reference] = ListPlus(),
        halfe_wave_potential: List[PotentialUnits] = ListPlus(),
        scan_rate: Optional[ScanRateUnits] = None,
        start_potential: Optional[PotentialUnits] = None,
        stop_potential: Optional[PotentialUnits] = None,
        potential_lower_limit: Optional[PotentialUnits] = None,
        potential_upper_limit: Optional[PotentialUnits] = None,
        i_pc_ox: List[CurrentUnits] = ListPlus(),
        i_pa_red: List[CurrentUnits] = ListPlus(),
        ox_potential_E_pc: List[PotentialUnits] = ListPlus(),
        red_potential_E_pa: List[PotentialUnits] = ListPlus(),
        total_cycle_number: Optional[int] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'CV' to attribute cv

        Args:
            id (str): Unique identifier of the 'CV' object. Defaults to 'None'.
            ferrocene_reference (): Parameters of the ferocene reference measurement. Defaults to ListPlus()
            halfe_wave_potential (): The half-wave potential of the measurement. Defaults to ListPlus()
            scan_rate (): The scan rate of the measurement. Defaults to None
            start_potential (): The starting value of the potential. Defaults to None
            stop_potential (): The stop value of the potential. Defaults to None
            potential_lower_limit (): The lower limit of the potential. Defaults to None
            potential_upper_limit (): The upper limit of the potential. Defaults to None
            i_pc_ox (): The current at the maximum of the cathodic peak (oxidation). Defaults to ListPlus()
            i_pa_red (): The current at the maximum of the anodic peak (reduction). Defaults to ListPlus()
            ox_potential_E_pc (): Potential at the maximum of the cathodic peak (reduction). Defaults to ListPlus()
            red_potential_E_pa (): The current at the maximum of the anodic peak (oxidation). Defaults to ListPlus()
            total_cycle_number (): The total cycle number. Defaults to None
        """

        params = {
            "ferrocene_reference": ferrocene_reference,
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

    def add_to_ca(
        self,
        induced_potential_first: Optional[PotentialUnits] = None,
        induced_potential_second: Optional[PotentialUnits] = None,
        time_duration: Optional[TimeUnits] = None,
        current_end_value: Optional[CurrentUnits] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'CA' to attribute ca

        Args:
            id (str): Unique identifier of the 'CA' object. Defaults to 'None'.
            induced_potential_first (): The first induced potential. Defaults to None
            induced_potential_second (): The second induced potential. Defaults to None
            time_duration (): The duration time of the induced potential. Defaults to None
            current_end_value (): The current value at the end of the measurement. Defaults to None
        """

        params = {
            "induced_potential_first": induced_potential_first,
            "induced_potential_second": induced_potential_second,
            "time_duration": time_duration,
            "current_end_value": current_end_value,
        }

        if id is not None:
            params["id"] = id

        self.ca.append(CA(**params))

    def add_to_cp(
        self,
        induced_current_first: Optional[CurrentUnits] = None,
        induced_current_second: Optional[CurrentUnits] = None,
        time_duration: Optional[TimeUnits] = None,
        potential_end_value: Optional[PotentialUnits] = None,
        charge_density: List[ChargeDensityUnits] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'CP' to attribute cp

        Args:
            id (str): Unique identifier of the 'CP' object. Defaults to 'None'.
            induced_current_first (): The first induced current. Defaults to None
            induced_current_second (): The first induced current. Defaults to None
            time_duration (): The duration time of the induced current. Defaults to None
            potential_end_value (): The potential value at the end of the measurement. Defaults to None
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
