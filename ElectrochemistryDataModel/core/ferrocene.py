import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .potential_units import Potential_units


@forge_signature
class Ferrocene(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("ferroceneINDEX"),
        xml="@id",
    )

    ox_potential_E_pc_ferrocene: Potential_units = Field(
        ...,
        description=(
            "Potential at the maximum of the cathodic peak (reduction) of the ferrocene"
            " reference"
        ),
    )

    red_potential_E_pa_ferrocene: Potential_units = Field(
        ...,
        description=(
            "The current at the maximum of the anodic peak (oxidation) of the ferrocene"
            " reference"
        ),
    )

    halfe_wave_potential_ferrocene: Potential_units = Field(
        ...,
        description="The half-wave potential of the ferrocene measurement",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8c095f77c03f72e972155264ab01c72d974f11c1"
    )
