import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Dataset_for_plots(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("dataset_for_plotsINDEX"),
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

    conducting_salt_concentration: Optional[str] = Field(
        default=None,
        description="The conducted_salt_concentration",
    )

    solvent: Optional[str] = Field(
        default=None,
        description="The solvent",
    )

    scan_rate: Optional[str] = Field(
        default=None,
        description="The scan rate",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="b242c4f4920848c0bb18a216bc42a917d186705b"
    )
