
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
    email: str
    password: str


class IssueBase(BaseModel):
    Issue_ID: int
    Student_ID: int
    Book_ID: int
    IssueDate: date 
    DueDate: date   
    ReturnDate: Optional[date] #it is optional as it will remain empty till the book is returned

class ShowBook(BaseModel):
    Name :str
    Author :str
    Genre :str
    PublicationYear :int
    ISBN :str

    class Config:
        from_attributes = True

class ShowStudent(BaseModel):
    Name :str
    Department :str
    YearOfStudy :int

    class Config:
        from_attributes = True

class ShowLibrarian(BaseModel):
    Name: str
    Designation: str

    class Config:
        from_attributes = True

class ShowLibrary(BaseModel):
    name: str
    address: str
    contact_number: str

    class Config:
        from_attributes = True

class ShowIssue(BaseModel):
    
    IssueDate: date 
    DueDate: date   
   
    class Config:
        from_attributes = True

class Login(BaseModel):
    username: str
    password: str
    #JWT needs username as the indentifier of the user but it is the same as email

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str]=None