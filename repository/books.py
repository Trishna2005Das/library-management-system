from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
import schemas,database,models
from sqlalchemy.orm import Session
# from hashing import Hash

def get_books(db:Session):
    book_list=db.query(models.Books).all()
    return book_list

def add_book(request: schemas.Bookbase, db: Session):
    new_book = models.Book(
        Book_ID=request.Book_ID,
        Name=request.Name,
        Quantity=request.Quantity,
        Author=request.Author,
        Genre=request.Genre,
        PublicationYear=request.PublicationYear,
        ISBN=request.ISBN
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def update_book(id:int, request: schemas.Bookbase, db: Session):
    book = db.query(models.Books).filter(models.Books.Book_ID == id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with id: {id} does not exist")
    book.update(request.dict())
    db.commit()
    return book

def delete_book(id:int, db: Session):
    book=db.query(models.Books).filter(models.Books.Book_ID==id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'book with id {id} is not available')
    book.delete(synchronize_session=False)
    db.commit()
    return 'done'

