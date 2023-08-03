from enum import Enum


class ReferenceElectrode(Enum):
    SHE = "SHE"
    RHE = "RHE"
    Ag_AgCl = "Ag/AgCl"
    Ag_AgSO4 = "Ag/Ag2SO4"
    Hg_HgO = "Hg/HgO"
    Hg_Hg2Cl2 = "Hg/Hg2Cl2"
    Hg_Hg2SO4 = "Hg/Hg2SO4"
    Fc_Fc = "Fc/Fc+"
