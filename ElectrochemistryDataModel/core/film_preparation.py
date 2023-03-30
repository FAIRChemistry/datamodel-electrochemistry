import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .spin_coating import Spin_coating
from .volume_units import Volume_units
from .time_units import Time_units
from .temperature_units import Temperature_units


@forge_signature
class Film_preparation(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("film_preparationINDEX"),
        xml="@id",
    )

    spin_coating: List[Spin_coating] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Spin coating parameter",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="14a8256647b8ffa4966fd852a28c3b80163565a9"
    )

    def add_spin_coating_to_spin_coating(
        self,
        volume: Volume_units,
        time: Time_units,
        rotation: List[float] = ListPlus(),
        annealing_temperature: Optional[Temperature_units] = None,
        annealing_time: Optional[Time_units] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Spin_coating' to attribute spin_coating

        Args:
            id (str): Unique identifier of the 'Spin_coating' object. Defaults to 'None'.
            volume (): The volume which was used for the film.
            time (): The rotation time.
            rotation (): The rotation speed of the spin coating process. Defaults to ListPlus()
            annealing_temperature (): The annealing temperature for the film. Defaults to None
            annealing_time (): The annealing time for the film. Defaults to None
        """

        params = {
            "volume": volume,
            "time": time,
            "rotation": rotation,
            "annealing_temperature": annealing_temperature,
            "annealing_time": annealing_time,
        }

        if id is not None:
            params["id"] = id

        self.spin_coating.append(Spin_coating(**params))
