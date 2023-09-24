import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .analysis import Analysis
from .sample import Sample
from .purging import Purging
from .experiment_type import Experiment_type
from .electrodesetup import ElectrodeSetup
from .electrolyte import Electrolyte


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

    sample: Optional[Sample] = Field(
        default=None,
        description="Information about the sample",
    )

    filename: Optional[str] = Field(
        default=None,
        description="Name of the experiment file (with the path)",
    )

    information: Optional[str] = Field(
        default=None,
        description="Information of the experiment",
    )

    electrode_setup: Optional[ElectrodeSetup] = Field(
        default=None,
        description="Name of the used electrode materials",
    )

    electrolyte: Optional[Electrolyte] = Field(
        default=None,
        description="The used electrolyte",
    )

    purging: Optional[Purging] = Field(
        default=None,
        description="The purging information for the experiment",
    )

    analysis: Optional[Analysis] = Field(
        default=None,
        description="The analysis type of the experiment",
    )

    type: Optional[Experiment_type] = Field(
        default=None,
        description="Type of experiment",
    )

    date_of_work: Optional[str] = Field(
        default=None,
        description="Date/time when the experiment was created",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="ba6aa04635d73779d00c7c6b39e863c4ba93ef80"
    )
