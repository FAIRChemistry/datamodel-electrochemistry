import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .volumeunits import VolumeUnits
from .temperatureunits import TemperatureUnits
from .timeunits import TimeUnits
from .spincoating import SpinCoating


@forge_signature
class FilmPreparation(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("filmpreparationINDEX"),
        xml="@id",
    )

    spin_coating: List[SpinCoating] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Spin coating parameter",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="a39428cabbbbcba7c89935626bf374b54c6f797a"
    )

    def add_to_spin_coating(
        self,
        volume: Optional[VolumeUnits] = None,
        rotation: List[float] = ListPlus(),
        time: Optional[TimeUnits] = None,
        annealing_temperature: Optional[TemperatureUnits] = None,
        annealing_time: Optional[TimeUnits] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'SpinCoating' to attribute spin_coating

        Args:
            id (str): Unique identifier of the 'SpinCoating' object. Defaults to 'None'.
            volume (): The volume which was used for the film. Defaults to None
            rotation (): The rotation speed of the spin coating process. Defaults to ListPlus()
            time (): The rotation time. Defaults to None
            annealing_temperature (): The annealing temperature for the film. Defaults to None
            annealing_time (): The annealing time for the film. Defaults to None
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

        self.spin_coating.append(SpinCoating(**params))
