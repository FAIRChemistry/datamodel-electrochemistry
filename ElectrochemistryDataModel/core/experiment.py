import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .purging import Purging
from .electrolyte import Electrolyte
from .analysis import Analysis
from .experiment_type import Experiment_type
from .electrodesetup import ElectrodeSetup
from .sample import Sample


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

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="1b2fb8a569b792ea51ff85ef5ca4c4cb080b4d71"
    )
