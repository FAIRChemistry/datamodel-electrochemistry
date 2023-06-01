import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .areaunits import AreaUnits
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

    WE_material: Optional[str] = Field(
        default=None,
        description="Name of the used working electrode material",
    )

    WE_area: Optional[AreaUnits] = Field(
        default=None,
        description="The area of the used working electrode",
    )

    type: Optional[Experiment_type] = Field(
        default=None,
        description="Type of experiment",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="ddd7d6672af897f07fe63fcc38cee589395d6df4"
    )
