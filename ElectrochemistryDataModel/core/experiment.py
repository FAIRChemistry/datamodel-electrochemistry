import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .electrolyte import Electrolyte
from .analysis import Analysis
from .electrodesetup import ElectrodeSetup
from .experiment_type import Experiment_type


@forge_signature
class Experiment(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("experimentINDEX"),
        xml="@id",
    )

    name: Optional[str] = Field(
        default=None,
        description="Name of the experiment",
    )

    filename: Optional[str] = Field(
        default=None,
        description="Name of the experiment file (with the path)",
    )

    electrode_setup: Optional[ElectrodeSetup] = Field(
        default=None,
        description="Name of the used electrode materials",
    )

    electrolyte: Optional[Electrolyte] = Field(
        default=None,
        description="The used electrolyte",
    )

    analysis: Optional[Analysis] = Field(
        default=None,
        description="The analysis type of the experiment",
    )

    type: Optional[Experiment_type] = Field(
        default=None,
        description="Type of experiment",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="2acb02b62b7f6a63829827e9feb609cd663e8a48"
    )
