from enum import Enum

class NiveauEnum(str, Enum):
    LO = "Loisir"
    DP = "Départemental"
    RG = "Régional"
    NA = "Nationale"
    P = "Pro"

class TypeSolEnum(str, Enum):
    H = "Herbe"
    S = "Salle"
    SB = "Sable"

class TypeTournoisEnum(str, Enum):
    ST = "Standard"
    N = "Nuit"

class TeamTypeEnum(str, Enum):
    team_2V = "2v2"
    team_3V = "3v3"
    team_4V = "4v4"
    team_6V = "6v6"

class Poste(str, Enum):
    passeur = "passeur"
    central = "central"
    pointu = "pointu"
    receptionneurAttaquant = "receptionneur-attaquant"
    libero = "libero"