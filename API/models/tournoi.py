from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from API.models.utils import *
from datetime import datetime
# Tournois model

class Tournois(BaseModel):
    BaseModel.model_config["arbitrary_types_allowed"] = True
    nom: str = Field(..., max_length=200)
    date: datetime.date = None
    lieu: str = Field(..., max_length=300)
    nombreEquipe: int = Field(...)
    departement: str = Field(..., max_length=300)
    nomOrganisateur: str = Field(..., max_length=300)
    emailOrganisateur: str
    telephone: str = Field(..., max_length=10)
    prixParEquipe: float = Field(...)
    heureDebut: datetime.time = None
    heureFin: datetime.time = None
    isMixte: bool = True
    isFood: bool = True # presence de buverie
    imageUrl: str | None
    niveau: NiveauEnum
    typeTournoi: TypeTournoisEnum
    typeSol: TypeSolEnum
    compositionEquipe: TeamTypeEnum | str

class UpdateTournois(BaseModel):
    BaseModel.model_config["arbitrary_types_allowed"] = True
    nom: Optional[str] = None
    date: Optional[datetime.date] = None
    lieu: Optional[str] = None 
    nombreEquipe: Optional[int] = None
    departement: Optional[str] = None 
    nomOrganisateur: Optional[str] = None 
    emailOrganisateur: Optional[str] = None
    telephone: Optional[str] = None 
    prixParEquipe: Optional[float] = None 
    heureDebut: Optional[datetime.time] = None 
    heureFin: Optional[datetime.time] = None 
    isMixte: Optional[bool] = True
    isFood: Optional[bool] = True # presence de buverie
    imageUrl: Optional[str | None] = None
    niveau: Optional[NiveauEnum] = None
    typeTournoi: Optional[TypeTournoisEnum] = None
    typeSol: Optional[TypeSolEnum] = None
    compositionEquipe: Optional[TeamTypeEnum | str] = None