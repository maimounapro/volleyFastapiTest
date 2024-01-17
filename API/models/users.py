from typing import Optional
from pydantic import BaseModel,Field
from API.models.utils import Poste

# User models

class CreateUser(BaseModel):
    nom: str = Field(min_length=1, max_length=16)
    age: str = Field(min_length=1, max_length=16)
    pseudo : str
    mdp: str
    taille: Optional[str] = None
    email: str
    created_at : str
    isActive: Optional[bool] = False
    poste: Poste