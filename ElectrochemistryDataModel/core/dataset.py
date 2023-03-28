import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from datetime import datetime
from pydantic import Field
from typing import List

from .parameter import Parameter


@forge_signature
class Dataset(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("datasetINDEX"),
        xml="@id",
    )
    name: str = Field(
        ...,
        description="Name of the dataset",
    )

    date: datetime = Field(
        ...,
        description="Date/time when the dataset was created",
    )

    parameter: List[Parameter] = Field(
        description="Name of the parameter",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="f9140a168ff03af2a895467198a6fb7086f1f069"
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
