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
        default="3b2ff760caea088f6a765fe8498dd9ccea93167d"
    )

    def add_to_cv(
        self,
        solvent: Optional[str] = None,
        conducting_salt: Optional[str] = None,
        conducting_salt_concentration: Optional[float] = None,
        scan_rate: Optional[float] = None,
        i_pc: Optional[float] = None,
        i_pa: Optional[float] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'CV' to the attribute 'cv'.

        Args:


            id (str): Unique identifier of the 'CV' object. Defaults to 'None'.


            solvent (Optional[str]): Name of the solvent. Defaults to None


            conducting_salt (Optional[str]): Name of the used salt. Defaults to None


            conducting_salt_concentration (Optional[float]): The half-wave potential of the measurement in V. Defaults to None


            scan_rate (Optional[float]): The scan rate of the measurement in mV/s. Defaults to None


            i_pc (Optional[float]): The current at the maximum of the cathodic peak in A. Defaults to None


            i_pa (Optional[float]): The current at the maximum of the anodic peak in A. Defaults to None
        """

        params = {
            "solvent": solvent,
            "conducting_salt": conducting_salt,
            "conducting_salt_concentration": conducting_salt_concentration,
            "scan_rate": scan_rate,
            "i_pc": i_pc,
            "i_pa": i_pa,
        }
        if id is not None:
            params["id"] = id
        cv = [CV(**params)]
        self.cv = self.cv + cv
