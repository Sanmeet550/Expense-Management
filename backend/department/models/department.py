from db import Base
from sqlalchemy import Column, Integer, String, Boolean, text


class Departments(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
