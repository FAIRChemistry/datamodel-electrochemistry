import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class DatasetForPlots(sdRDM.DataModel):

    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("datasetforplotsINDEX"),
        xml="@id",
    )

    filename: Optional[str] = Field(
        default=None,
        description="The filename with path",
    )

    reference: Optional[str] = Field(
        default=None,
        description="The reference",
    )

    name: Optional[str] = Field(
        default=None,
        description="The name",
    )

    conducting_salt: Optional[str] = Field(
        default=None,
        description="The conducting_salt",
    )

    concentration: Optional[str] = Field(
        default=None,
        description="The conducted_salt_concentration",
    )

    solvent: Optional[str] = Field(
        default=None,
        description="The solvent",
    )

    pH: Optional[str] = Field(
        default=None,
        description="The pH value",
    )

    scan_rate: Optional[str] = Field(
        default=None,
        description="The scan rate",
    )

    substrate: Optional[str] = Field(
        default=None,
        description="name of the substrate (WE)",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="cb12f3561b0b49f85f04d80dd56ea6af4d04f764"
    )
