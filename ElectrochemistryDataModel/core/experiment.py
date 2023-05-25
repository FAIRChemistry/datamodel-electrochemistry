import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .areaunits import AreaUnits


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

    WE_material: Optional[str] = Field(
        default=None,
        description="Name of the used working electrode material",
    )

    WE_area: Optional[AreaUnits] = Field(
        default=None,
        description="The area of the used working electrode",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8867c2a3e77fe6c21d29d56abe5a449b7d1454cb"
    )
