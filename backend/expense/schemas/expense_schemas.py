from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional, List
from expense.schemas.expense_report_schemas import ExpenseReportSchemas


class ExpenseSchemas(BaseModel):
    name: str
    total: Optional[float]
    expense_date: Optional[date]
    description: Optional[str] = Field(None, max_length=255)
    created_on: Optional[datetime] = Field(..., description='Created Date')
    category_id: int = Field(None,
                             description='Foreign key to ExpenseCategory')

    report_id: Optional[int] = None
    report_ids: Optional[List[ExpenseReportSchemas]] = []

    class config:
        orm = True


class InheritExpenseReportSchemas(ExpenseReportSchemas):
    expense_ids: Optional[List[ExpenseSchemas]] = []
