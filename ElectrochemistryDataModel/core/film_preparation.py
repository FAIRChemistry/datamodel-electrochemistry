import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .spin_coating import Spin_coating


@forge_signature
class Film_preparation(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("film_preparationINDEX"),
        xml="@id",
    )

    spin_coating: List[Spin_coating] = Field(
        multiple=True,
        description="Spin coating parameter",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="947d6e485af252858b1b3c61b6f067dcf951dca0"
    )

    def add_spin_coating_to_spin_coating(
        self, volume: float, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'Spin_coating' to attribute spin_coating

        Args:
            id (str): Unique identifier of the 'Spin_coating' object. Defaults to 'None'.
            volume (): The volume which was used for the film.
        """

        params = {
            "volume": volume,
        }

        if id is not None:
            params["id"] = id

        self.spin_coating.append(Spin_coating(**params))
