from db import Base
from sqlalchemy import Column, String, Integer, Float


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
