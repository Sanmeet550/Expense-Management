from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from users.schemas.users_schemas import UsersSchemas
from db import get_db, Base
from users.models.users import Users


router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/create')
async def create_users(user: UsersSchemas, db: Session = Depends(get_db)):
    user_create = Users(name=user.name)
    db.add(user_create)
    db.commit()
    db.refresh(user_create)

    return user_create


@router.get('/all_users')
async def get_all_users(db: Session = Depends(get_db)):
    users_data = db.query(Users).all()
    return users_data


@router.put('/users/{user_id}')
async def single_department(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Users).filter(
        Users.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Item not found")
    return user


@router.delete("/users/{user_id}")
async def delete_department(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Users).filter(
        Users.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(user)
    db.commit()
    return {'message': 'Deleted Successfully'}
