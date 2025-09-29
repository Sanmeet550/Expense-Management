from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from department.schemas.department_schema import DepartmentsBase
from db import get_db, Base
from department.models.department import Departments


router = APIRouter(prefix='/department', tags=['Department'])


@router.post('/create')
async def create_department(department: DepartmentsBase, db: Session = Depends(get_db)):
    db_department = Departments(name=department.name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)

    return db_department


@router.get('/all_department')
async def get_all_department(db: Session = Depends(get_db)):
    departments_data = db.query(Departments).all()
    return departments_data


@router.put('department/{department_id}')
async def single_department(department_id: int, db: Session = Depends(get_db)):
    depart = db.query(Departments).filter(
        Departments.id == department_id).first()
    if not depart:
        raise HTTPException(status_code=404, detail="Item not found")
    return depart


@router.delete("/department/{department_id}")
async def delete_department(department_id: int, db: Session = Depends(get_db)):
    department = db.query(Departments).filter(
        Departments.id == department_id).first()
    if not department:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(department)
    db.commit()
    return {'message': 'Deleted Successfully'}
