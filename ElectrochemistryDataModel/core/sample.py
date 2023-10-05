import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .timeunits import TimeUnits
from .temperatureunits import TemperatureUnits
from .purging import Purging
from .pressureunits import PressureUnits
from .molecularweightunits import MolecularWeightUnits
from .filmpreparation import FilmPreparation
from .synthesis import Synthesis


@forge_signature
class Sample(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("sampleINDEX"),
        xml="@id",
    )

    name_product: Optional[str] = Field(
        default=None,
        description="The name of the product",
    )

    chemical_formula: Optional[str] = Field(
        default=None,
        description="The chemical formula of the product",
    )

    molecular_weight: Optional[MolecularWeightUnits] = Field(
        default=None,
        description="The molecular weight of the product",
    )

    synthesis: List[Synthesis] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="The synthesis of the product",
    )

    film_preparation: Optional[FilmPreparation] = Field(
        default=None,
        description="The film preparation of the product",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel-electrochemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="683376ca9e7631a0eec2a69d9aa8a1d1e3a9a01e"
    )

    def add_to_synthesis(
        self,
        reagents: Optional[str] = None,
        solvent: Optional[str] = None,
        reaction_time: Optional[float] = None,
        reaction_time_unit: Optional[TimeUnits] = None,
        reaction_temperature: Optional[float] = None,
        reaction_temperature_unit: Optional[TemperatureUnits] = None,
        reaction_pressure: Optional[float] = None,
        reaction_pressure_unit: Optional[PressureUnits] = None,
        purging: Optional[Purging] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Synthesis' to attribute synthesis

        Args:
            id (str): Unique identifier of the 'Synthesis' object. Defaults to 'None'.
            reagents (): The reagents of the product. Defaults to None
            solvent (): The solvent of the synthesis. Defaults to None
            reaction_time (): The reaction time. Defaults to None
            reaction_time_unit (): The reaction time. Defaults to None
            reaction_temperature (): The reaction temperature. Defaults to None
            reaction_temperature_unit (): The reaction temperature unit. Defaults to None
            reaction_pressure (): The reaction pressure. Defaults to None
            reaction_pressure_unit (): The reaction pressure unit. Defaults to None
            purging (): The purging information for the synthesis experiment. Defaults to None
        """

        params = {
            "reagents": reagents,
            "solvent": solvent,
            "reaction_time": reaction_time,
            "reaction_time_unit": reaction_time_unit,
            "reaction_temperature": reaction_temperature,
            "reaction_temperature_unit": reaction_temperature_unit,
            "reaction_pressure": reaction_pressure,
            "reaction_pressure_unit": reaction_pressure_unit,
            "purging": purging,
        }

        if id is not None:
            params["id"] = id

        self.synthesis.append(Synthesis(**params))
