import sdRDM

from typing import Optional, Union
from typing import List
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from datetime import datetime
from .parameter import Parameter
from .author import Author


@forge_signature
class Dataset(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("datasetINDEX"),
        xml="@id",
    )

    name: str = Field(..., description="Name of the dataset")

    parameter: List[Parameter] = Field(
        description="Name of the parameter", default_factory=ListPlus
    )

    date: Optional[datetime] = Field(
        description="Date/time when the dataset was created", default=None
    )

    author: List[Author] = Field(
        description="Persons who worked on the dataset", default_factory=ListPlus
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="51895a81cf68d0ad170cee3cd6f1d9fca991cc9e"
    )

    def add_to_parameter(
        self,
        solvent: str,
        conducting_salt: str,
        scan_rate: int,
        working_electrode: str,
        reference: str,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Parameter' to the attribute 'parameter'.

        Args:


            id (str): Unique identifier of the 'Parameter' object. Defaults to 'None'.


            solvent (str): Name of the solvent.


            conducting_salt (str): Name of the used salt.


            scan_rate (int): Name of the used scan rate.


            working_electrode (str): Name of the used working electrode.


            reference (str): Name of the reference.
        """

        params = {
            "solvent": solvent,
            "conducting_salt": conducting_salt,
            "scan_rate": scan_rate,
            "working_electrode": working_electrode,
            "reference": reference,
        }
        if id is not None:
            params["id"] = id
        parameter = [Parameter(**params)]
        self.parameter = self.parameter + parameter

    def add_to_author(
        self,
        name: Optional[str] = None,
        affiliation: Optional[str] = None,
        email: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Author' to the attribute 'author'.

        Args:


            id (str): Unique identifier of the 'Author' object. Defaults to 'None'.


            name (Optional[str]): Full name of the author. Defaults to None


            affiliation (Optional[str]): Organisation the author is affiliated with. Defaults to None


            email (Optional[str]): Contact e-mail address of the author. Defaults to None
        """

        params = {"name": name, "affiliation": affiliation, "email": email}
        if id is not None:
            params["id"] = id
        author = [Author(**params)]
        self.author = self.author + author
