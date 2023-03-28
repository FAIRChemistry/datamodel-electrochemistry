import sdRDM

from typing import Optional, Union
from typing import Optional
from typing import List
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .cv import CV
from .cp import CP


@forge_signature
class Analysis(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("analysisINDEX"),
        xml="@id",
    )

    cv: List[CV] = Field(description="cv", default_factory=ListPlus)

    cp: List[CP] = Field(description="cp", default_factory=ListPlus)

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="2bdc6aeb99c7d4e0a78a3c95e6a38cae88df8fdd"
    )

    def add_to_cv(
        self,
        solvent: Optional[str] = None,
        conducting_salt: Optional[str] = None,
        total_cycle_number: Optional[int] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'CV' to the attribute 'cv'.

        Args:


            id (str): Unique identifier of the 'CV' object. Defaults to 'None'.


            solvent (Optional[str]): Name of the solvent. Defaults to None


            conducting_salt (Optional[str]): Name of the used salt. Defaults to None


            total_cycle_number (Optional[int]): The total cycle number. Defaults to None
        """

        params = {
            "solvent": solvent,
            "conducting_salt": conducting_salt,
            "total_cycle_number": total_cycle_number,
        }
        if id is not None:
            params["id"] = id
        cv = [CV(**params)]
        self.cv = self.cv + cv

    def add_to_cp(
        self,
        solvent: Optional[str] = None,
        conducting_salt: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'CP' to the attribute 'cp'.

        Args:


            id (str): Unique identifier of the 'CP' object. Defaults to 'None'.


            solvent (Optional[str]): Name of the solvent. Defaults to None


            conducting_salt (Optional[str]): Name of the used salt. Defaults to None
        """

        params = {"solvent": solvent, "conducting_salt": conducting_salt}
        if id is not None:
            params["id"] = id
        cp = [CP(**params)]
        self.cp = self.cp + cp
