from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
import schemas,database,models
from sqlalchemy.orm import Session
# from hashing import Hash


def get_students(db:Session):
    student_list=db.query(models.Students).all()
    return student_list

def add_student(request: schemas.StudentBase, db: Session):
    new_student = models.Student(
        Student_ID=request.Student_ID,
        Name=request.Name,
        Department=request.Department,
        YearOfStudy=request.YearOfStudy,
        ContactNumber=request.ContactNumber
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def update_student(id:int, request: schemas.StudentBase, db: Session):
    student = db.query(models.Students).filter(models.Students.Student_ID == id)
    if not student.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Student with id: {id} does not exist")
    student.update(request.dict())
    db.commit()
    return student

def delete_student(id:int,db:Session):
    student=db.query(models.Students).filter(models.Students.Student_ID==id)
    if not student.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'student with id {id} is not available')
    student.delete(synchronize_session=False)
    db.commit()
    return 'done'