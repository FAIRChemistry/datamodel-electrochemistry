import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .experiment_type import Experiment_type
from .areaunits import AreaUnits
from .electrodesetup import ElectrodeSetup


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

    WE_material: Optional[str] = Field(
        default=None,
        description="Name of the used working electrode material",
    )

    WE_area: Optional[AreaUnits] = Field(
        default=None,
        description="The area of the used working electrode",
    )

    solvent_test: Optional[str] = Field(
        default=None,
        description="Name of the solvent",
    )

    electrode_setup_test: Optional[ElectrodeSetup] = Field(
        default=None,
        description="Name of the used electrode materials",
    )

    type: Optional[Experiment_type] = Field(
        default=None,
        description="Type of experiment",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="335acb05751730a5198440bdad0c7b9bb4896787"
    )
