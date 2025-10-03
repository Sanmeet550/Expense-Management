from fastapi import FastAPI
from db import engine, Base
from department.api.department_api import router as department_router
from department.models.department import Departments
from expense.models.expense_category import ExpenseCategory
from expense.models.expense import Expense
from expense.models.expense_report import ExpenseReport
from users.models.users import Users
from expense.api.expense_category_api import router as expense_cat_router
from expense.api.expense_api import router as expense
from users.api.users_api import router as users
from expense.api.expense_report_api import router as expense_report


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(department_router)
app.include_router(expense_cat_router)
app.include_router(expense)
app.include_router(expense_report)
app.include_router(users)


@app.get('/')
async def root():
    return {"message": "Hello world"}
