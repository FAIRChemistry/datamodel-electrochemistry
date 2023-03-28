import sdRDM

from typing import Optional, Union
from typing import Optional
from typing import List
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .cv import CV


@forge_signature
class Analysis(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("analysisINDEX"),
        xml="@id",
    )

    cv: List[CV] = Field(description="cv", default_factory=ListPlus)

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="615441ab6cb6d376edde4cf0afb09fdbd20d2d34"
    )

    def add_to_cv(
        self,
        solvent: Optional[str] = None,
        conducting_salt: Optional[str] = None,
        conducting_salt_concentration: Optional[float] = None,
        halfe_wave_potential: Optional[float] = None,
        scan_rate: Optional[float] = None,
        start_potential: Optional[float] = None,
        stop_potential: Optional[float] = None,
        i_pc: Optional[float] = None,
        i_pa: Optional[float] = None,
        potential_E_pc: Optional[float] = None,
        potential_E_pa: Optional[float] = None,
        total_cycle_number: Optional[int] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'CV' to the attribute 'cv'.

        Args:


            id (str): Unique identifier of the 'CV' object. Defaults to 'None'.


            solvent (Optional[str]): Name of the solvent. Defaults to None


            conducting_salt (Optional[str]): Name of the used salt. Defaults to None


            conducting_salt_concentration (Optional[float]): Concentration of the conducting salt in mol/l. Defaults to None


            halfe_wave_potential (Optional[float]): The half-wave potential of the measurement in V. Defaults to None


            scan_rate (Optional[float]): The scan rate of the measurement in mV/s. Defaults to None


            start_potential (Optional[float]): The starting value of the potential in V. Defaults to None


            stop_potential (Optional[float]): The stop value of the potential in V. Defaults to None


            i_pc (Optional[float]): The current at the maximum of the cathodic peak in A. Defaults to None


            i_pa (Optional[float]): The current at the maximum of the anodic peak in A. Defaults to None


            potential_E_pc (Optional[float]): Potential at the maximum of the cathodic peak in V. Defaults to None


            potential_E_pa (Optional[float]): The current at the maximum of the anodic peak in V. Defaults to None


            total_cycle_number (Optional[int]): The total cycle number. Defaults to None
        """

        params = {
            "solvent": solvent,
            "conducting_salt": conducting_salt,
            "conducting_salt_concentration": conducting_salt_concentration,
            "halfe_wave_potential": halfe_wave_potential,
            "scan_rate": scan_rate,
            "start_potential": start_potential,
            "stop_potential": stop_potential,
            "i_pc": i_pc,
            "i_pa": i_pa,
            "potential_E_pc": potential_E_pc,
            "potential_E_pa": potential_E_pa,
            "total_cycle_number": total_cycle_number,
        }
        if id is not None:
            params["id"] = id
        cv = [CV(**params)]
        self.cv = self.cv + cv
