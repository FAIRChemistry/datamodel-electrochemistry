from enum import Enum


class ConcentrationUnits(Enum):
    MOLAR = "mole / l"
    MILLI_MOLAR = "mmole / l"
    MICRO_MOLAR = "umole / l"
    NANO_MOLAR = "nmole / l"
    GRAM_LITER = "g / l"
    MILLIGRAM_LITER = "mg / l"
    MICROGRAM_LITER = "ug / l"
    NANGRAM_LITER = "ng / l"
