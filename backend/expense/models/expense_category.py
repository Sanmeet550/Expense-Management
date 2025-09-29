from fastapi import FastAPI
from db import Base
from sqlalchemy import Integer, String, Boolean, Column, Float


class ExpenseCategory(Base):
    __tablename__ = 'expense.category'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
