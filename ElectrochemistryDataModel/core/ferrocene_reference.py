import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .potentialunits import PotentialUnits


@forge_signature
class Ferrocene_reference(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("ferrocene_referenceINDEX"),
        xml="@id",
    )

    ox_potential_E_pc_ferrocene: Optional[PotentialUnits] = Field(
        default=None,
        description=(
            "Potential at the maximum of the cathodic peak (reduction) of the ferrocene"
            " reference"
        ),
    )

    red_potential_E_pa_ferrocene: Optional[PotentialUnits] = Field(
        default=None,
        description=(
            "The current at the maximum of the anodic peak (oxidation) of the ferrocene"
            " reference"
        ),
    )

    halfe_wave_potential_ferrocene: Optional[PotentialUnits] = Field(
        default=None,
        description="The half-wave potential of the ferrocene measurement",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="143c1d00d2f7fc62ddb6fee2f822f60c176785b7"
    )
