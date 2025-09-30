from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from expense.schemas.expense_schemas import ExpenseSchemas
from db import get_db
from expense.models.expense import Expense

router = APIRouter(prefix='/expense', tags=['Expense'])


@router.post('/create')
async def create(expense: ExpenseSchemas, db: Session = Depends(get_db)):
    exp_category = Expense(**expense.dict())
    db.add(exp_category)
    db.commit()
    db.refresh(exp_category)

    return {'message': 'Created Successfully', 'data': exp_category}


@router.get('/all-expense')
async def get_all_data(expense: ExpenseSchemas, db: Session = Depends(get_db)):
    expense = db.query(Expense).all()
    return expense


@router.put('/expense/{expense_id}')
async def single_expense(expense_id: int, expense: ExpenseSchemas, db: Session = Depends(get_db)):
    exp = db.query(Expense).filter(Expense.id == expense_id).first()
    if not exp:
        raise HTTPException(status_code=404, detail="Item not found")
    return exp


@router.delete("/expense/{expense_id}")
async def delete_department(expense_id: int, db: Session = Depends(get_db)):
    exp = db.query(Expense).filter(
        Expense.id == expense_id).first()
    if not exp:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(exp)
    db.commit()
    return {'message': 'Deleted Successfully'}
