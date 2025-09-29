from pydantic import BaseModel
from typing import Optional


class ExpenseCategoryBase(BaseModel):
    name: str
    cost: Optional[float]

    class Config():
        orm = True
