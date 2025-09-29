from pydantic import BaseModel


class DepartmentsBase(BaseModel):
    name: str

    class Config:
        orm_mode = True
