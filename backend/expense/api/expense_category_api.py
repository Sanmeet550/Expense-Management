from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from expense.schemas.expense_category_schemas import ExpenseCategoryBase
from db import get_db
from expense.models.expense_category import ExpenseCategory

router = APIRouter(prefix='/expense-category', tags=['Expense Category'])


@router.post('/create')
async def create(category: ExpenseCategoryBase, db: Session = Depends(get_db)):
    exp_category = ExpenseCategory(**category.dict())
    db.add(exp_category)
    db.commit()
    db.refresh(exp_category)

    return {'message': 'Created Successfully', 'data': exp_category}


@router.get('/all-category')
async def get_all_category(db: Session = Depends(get_db)):
    all_data = db.query(ExpenseCategory).all()
    return all_data


@router.put('expense-category/{category_id}')
async def single_category(category_id: int, db: Session = Depends(get_db)):
    single_category = db.query(ExpenseCategory).filter(
        ExpenseCategory.id == category_id).first()
    if not single_category:
        raise HTTPException(status_code=404, detail="Item not found")
    return single_category


@router.delete("/expense-category/{category_id}")
async def delete_department(category_id: int, db: Session = Depends(get_db)):
    exp_category = db.query(ExpenseCategory).filter(
        ExpenseCategory.id == category_id).first()
    if not exp_category:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(exp_category)
    db.commit()
    return {'message': 'Deleted Successfully'}
