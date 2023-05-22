import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Experiment(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("experimentINDEX"),
        xml="@id",
    )

    experiment_name: Optional[str] = Field(
        default=None,
        description="Name of the experiment",
    )

    experiment_filename: Optional[str] = Field(
        default=None,
        description="Name of the experiment file (with the path)",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="beca177b218acaffb6190e8f60815c5bd7ce553e"
    )
