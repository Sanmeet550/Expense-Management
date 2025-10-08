from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from expense.schemas.expense_report_schemas import ExpenseReportSchemas
from expense.models.expense_report import ExpenseReport


router = APIRouter(prefix='/expense-report', tags=['Expense Report'])


@router.post('/create')
async def create_report(expense_report: ExpenseReportSchemas, db: Session = Depends(get_db)):
    exp_report = ExpenseReport(**expense_report.dict())
    db.add(exp_report)
    db.commit()
    db.refresh(exp_report)
    return {'message': 'Created Successfully', 'data': exp_report}
