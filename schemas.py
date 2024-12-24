
from pydantic import BaseModel
from typing import List,Optional
from datetime import date
#there are two types of model sqlalchemy and pydantic
#the pydantic model is used to create the schema for the api


class Bookbase(BaseModel):
    
    Book_ID :int
    Name :str
    Quantity :int
    Author :str
    Genre :str
    PublicationYear :int
    ISBN :str
    
class StudentBase(BaseModel):
    Student_ID :int
    Name :str
    Department :str
    YearOfStudy :int
    ContactNumber :str
    
class LibrarianBase(BaseModel):
    Librarian_ID: int
    Name: str
    Designation: str
    ContactNumber: str


class IssueBase(BaseModel):
    Issue_ID: int
    Student_ID: int
    Book_ID: int
    IssueDate: date 
    DueDate: date   
    ReturnDate: Optional[date] #it is optional as it will remain empty till the book is returned