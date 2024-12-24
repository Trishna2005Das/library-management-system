from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
import schemas,database,models,oauth2 #routers directory which is inside blog directory 
from sqlalchemy.orm import Session
from repository import books
get_db=database.get_db
router=APIRouter(
    prefix="/books",
    tags=['Books Table'])

@router.get('/check_book',response_model=List[schemas.Bookbase])
def book_all(db:Session=Depends(get_db)):
    return books.get_books(db)
@router.post('/books', response_model=schemas.Bookbase)
def add_book(request: schemas.Bookbase, db: Session = Depends(get_db)):
    return books.add_book(request, db)

@router.put('/books/{id}', response_model=schemas.Bookbase)
def update_book(id:int, request: schemas.Bookbase, db: Session = Depends(get_db)):
    return books.update_book(id, request, db)

@router.delete('/books/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id:int, db: Session = Depends(get_db)):
    return books.delete_book(id, db)