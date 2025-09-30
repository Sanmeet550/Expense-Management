from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional


class ExpenseSchemas(BaseModel):
    name: str
    total: Optional[float]
    expense_date: Optional[date]
    description: Optional[str] = Field(None, max_length=255)
    created_on: Optional[datetime] = Field(..., description='Created Date')
    category_id: int = Field(None,
                             description='Foreign key to ExpenseCategory')

    class config:
        orm = True
