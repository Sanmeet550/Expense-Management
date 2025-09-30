from db import Base
from sqlalchemy import Column, String, Float, Integer, Text, Date, ForeignKey,DateTime


class Expense(Base):
    __tablename__ = 'expense'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    total = Column(Float, nullable=False)
    expense_date = Column(Date)
    description = Column(Text)
    created_on = Column(DateTime)
    category_id = Column(Integer, ForeignKey('expense_category.id'))
