from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
import schemas,database,models,oauth2 #routers directory which is inside blog directory 
from sqlalchemy.orm import Session
from repository import librarians
get_db=database.get_db
router=APIRouter(
    prefix="/librarians",
    tags=[' Librarians Table'])

@router.get('/',response_model=List[schemas.LibrarianBase])
def librarian_all(db:Session=Depends(get_db)):
    return librarians.get_librarians(db)

@router.post('/', response_model=schemas.ShowLibrarian)
def add_librarian(request: schemas.LibrarianBase, db: Session = Depends(get_db)):
    return librarians.add_librarian(request, db)


@router.put('/{id}', response_model=schemas.ShowLibrarian)
def update_librarian(id:int, request: schemas.LibrarianBase, db: Session = Depends(get_db)):
    return librarians.update_librarian(id, request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_librarian(id:int, db: Session = Depends(get_db)):
    return librarians.delete_librarian(id, db)