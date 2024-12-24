from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
import schemas,database,models,oauth2 #routers directory which is inside blog directory 
from sqlalchemy.orm import Session
from repository import students
get_db=database.get_db
router=APIRouter(
    prefix="/ students",
    tags=[' Students Table'])

@router.get('/check',response_model=List[schemas.StudentBase])
def student_all(db:Session=Depends(get_db)):
    return students.get_students(db)

@router.post('/create', response_model=schemas.StudentBase)
def add_student(request: schemas.StudentBase, db: Session = Depends(get_db)):
    return students.add_student(request, db)


@router.put('/students/{id}', response_model=schemas.StudentBase)
def update_student(id:int, request: schemas.StudentBase, db: Session = Depends(get_db)):
    return students.update_student(id, request, db)


@router.delete('/students/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id:int, db: Session = Depends(get_db)):
    return students.delete_student(id, db)