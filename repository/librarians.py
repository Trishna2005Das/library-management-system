from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
import schemas,database,models
from sqlalchemy.orm import Session
# from hashing import Hash

def get_librarians(db:Session):
    librarian_list=db.query(models.Librarians).all()
    return librarian_list


def add_librarian(request: schemas.LibrarianBase, db: Session):
    new_librarian = models.Librarian(
        Librarian_ID=request.Librarian_ID,
        Name=request.Name,
        Designation=request.Designation,
        ContactNumber=request.ContactNumber
    )
    db.add(new_librarian)
    db.commit()
    db.refresh(new_librarian)
    return new_librarian

def update_librarian(id:int, request: schemas.LibrarianBase, db: Session):
    librarian = db.query(models.Librarians).filter(models.Librarians.Librarian_ID == id)
    if not librarian.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Librarian with id: {id} does not exist")
    librarian.update(request.dict())
    db.commit()
    return librarian

def delete_librarian(id:int,db:Session):
    librarian=db.query(models.Librarians).filter(models.Librarians.Librarian_ID==id)
    if not librarian.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'librarian with id {id} is not available')
    librarian.delete(synchronize_session=False)
    db.commit()
    return 'done'


