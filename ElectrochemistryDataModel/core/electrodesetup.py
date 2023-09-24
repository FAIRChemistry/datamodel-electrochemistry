import sdRDM

from typing import Optional, Union
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .concentrationunits import ConcentrationUnits
from .referenceelectrode import ReferenceElectrode
from .areaunits import AreaUnits


@forge_signature
class ElectrodeSetup(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("electrodesetupINDEX"),
        xml="@id",
    )

    working_electrode: Optional[str] = Field(
        default=None,
        description="Name of the used working electrode",
    )

    working_electrode_area: Optional[float] = Field(
        default=None,
        description="The area of the used working electrode",
    )

    working_electrode_area_unit: Optional[AreaUnits] = Field(
        default=None,
        description="The area of the used working electrode",
    )

    counter_electrode: Optional[str] = Field(
        default=None,
        description="Name of the used counter electrode",
    )

    reference_electrode: Optional[ReferenceElectrode] = Field(
        default=None,
        description="Name of the used reference electrode",
    )

    reference_electrode_salt: Optional[str] = Field(
        default=None,
        description="Name of the reference salt",
    )

    reference_electrode_salt_concentration: Union[float, str, None] = Field(
        default=None,
        description="Unit of the reference salt concentration",
    )

    reference_electrode_salt_concentration_unit: Optional[ConcentrationUnits] = Field(
        default=None,
        description="Unit of the reference salt concentration",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="a1c6eab16e0b0b7e3ab6aa62c9f1d897ddab5d5f"
    )
