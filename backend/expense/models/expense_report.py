from db import Base
from sqlalchemy import Column, String, Boolean, Date, DateTime, Integer
from sqlalchemy.orm import relationship


class ExpenseReport(Base):
    __tablename__ = 'expense_report'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # We write here the model name
    # IN back populate we write the field name of the other model you want to sync
    expense_ids = relationship("Expense", back_populates='report_ids')
