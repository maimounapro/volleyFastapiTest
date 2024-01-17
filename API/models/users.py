from typing import Optional
from pydantic import BaseModel, Field
from API.models.utils import Poste
from datetime import date, datetime
# User models

class User(BaseModel):
    pseudo : str
    age: int
    email: str
    taille: Optional[int] = None
    created_at : Optional[datetime] = datetime.combine(date.today(), datetime.min.time())
    isActive: Optional[bool] = True
    poste: Poste

class UserInDB(User):
    hashedPassword: str

    def setHashedPassword(self, password):
        self.hashedPassword = password