from fastapi import FastAPI
from db import engine, Base
from department.api.department_api import router as department_router
from department.models.department import Departments
from expense.models.expense_category import ExpenseCategory
from expense.api.expense_category_api import router as expense_cat_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(department_router)
app.include_router(expense_cat_router)


@app.get('/')
async def root():
    return {"message": "Hello world"}
