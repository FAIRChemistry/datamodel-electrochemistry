import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class PotentialEndValue(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("potentialendvalueINDEX"),
        xml="@id",
    )

    method: Optional[str] = Field(
        default=None,
        description="The method, which was used to determine this value",
    )

    end_value: Optional[float] = Field(
        default=None,
        description="The end value potential",
    )

    reference_name: Optional[str] = Field(
        default=None,
        description="The used reference scale",
    )

    change_reference_potential: Optional[float] = Field(
        default=None,
        description="The change_reference potential",
    )

    last_average_points: Optional[int] = Field(
        default=None,
        description="The last points, which were used to calculate the average",
    )

    fit_function: Optional[str] = Field(
        default=None,
        description="The fit function, if the fit function was used",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="a1c6eab16e0b0b7e3ab6aa62c9f1d897ddab5d5f"
    )
