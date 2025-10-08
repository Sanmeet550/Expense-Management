from pydantic import BaseModel
from typing import Optional, List


class ExpenseReportSchemas(BaseModel):
    name: str

    class Config():
        orm = True
