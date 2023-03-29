import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .time_units import Time_units
from .spin_coating import Spin_coating
from .volume_units import Volume_units
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
        multiple=True,
        description="Spin coating parameter",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="edef7869f99e64d12287be211045677c3ae889fa"
    )

    def add_spin_coating_to_spin_coating(
        self,
        volume: Volume_units,
        rotation: float,
        time: Time_units,
        annealing_temperature: Temperature_units,
        annealing_time: Time_units,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Spin_coating' to attribute spin_coating

        Args:
            id (str): Unique identifier of the 'Spin_coating' object. Defaults to 'None'.
            volume (): The volume which was used for the film.
            rotation (): The rotation speed for the film.
            time (): The rotation time.
            annealing_temperature (): The anealing temperature for the film.
            annealing_time (): The anealing time for the film.
        """

        params = {
            "volume": volume,
            "rotation": rotation,
            "time": time,
            "annealing_temperature": annealing_temperature,
            "annealing_time": annealing_time,
        }

        if id is not None:
            params["id"] = id

        self.spin_coating.append(Spin_coating(**params))
