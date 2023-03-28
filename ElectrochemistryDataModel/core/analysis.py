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
        default="827b9d7f19851a081cf41ba2e9af9f1b707e5a38"
    )

    def add_to_cv(
        self,
        solvent: Optional[str] = None,
        conducting_salt: Optional[str] = None,
        conducting_salt_concentration: Optional[float] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'CV' to the attribute 'cv'.

        Args:


            id (str): Unique identifier of the 'CV' object. Defaults to 'None'.


            solvent (Optional[str]): Name of the solvent. Defaults to None


            conducting_salt (Optional[str]): Name of the used salt. Defaults to None


            conducting_salt_concentration (Optional[float]): Concentration of the conducting salt in mol/l. Defaults to None
        """

        params = {
            "solvent": solvent,
            "conducting_salt": conducting_salt,
            "conducting_salt_concentration": conducting_salt_concentration,
        }
        if id is not None:
            params["id"] = id
        cv = [CV(**params)]
        self.cv = self.cv + cv
