from typing import Optional
from pydantic import BaseModel,Field
from API.models.utils import Poste
import datetime
# User models

class CreateUser(BaseModel):
    nom: str = Field(min_length=1, max_length=16)
    age: str = Field(min_length=1, max_length=16)
    pseudo : str
    mdp: str
    taille: Optional[str] = None
    email: str
    created_at : Optional[datetime.date] = datetime.date.today()
    isActive: Optional[bool] = True
    poste: Poste