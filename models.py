from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from database import Base
from sqlalchemy.orm import relationship

class Books(Base):
    __tablename__ = 'Books'

    Book_ID = Column(Integer, primary_key=True, index=True)
    Title = Column(String)
    AuthNo = Column(String)
    Category = Column(String)
    Edition = Column(String)
    Price = Column(Float)
    ISBN = Column(String)

class Readers(Base):
    __tablename__ = 'Readers'

    User_ID = Column(Integer, primary_key=True, index=True)
    Firstname = Column(String)
    Lastname = Column(String)
    Email = Column(String)
    Address = Column(String)
    Phone_No = Column(String)
    login=relationship("Authentication",back_populates="enter")

class Staff(Base):
    __tablename__ = 'Staff'

    Staff_ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)

class Publisher(Base):
    __tablename__ = 'Publisher'

    Publisher_ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    YearOfPublication = Column(Integer)

class Authentication(Base):
    __tablename__ = 'Authentication'

    LoginID = Column(Integer, primary_key=True, index=True)
    Password = Column(String)
    User_ID = Column(Integer, ForeignKey('Readers.User_ID'))
    
    enter=relationship("Authentication",back_populates="login")

class Reports(Base):
    __tablename__ = 'Reports'

    Reg_No = Column(Integer, primary_key=True, index=True)
    Book_No = Column(Integer, ForeignKey('Books.Book_ID'))
    Issue_Return = Column(String)
    User_ID = Column(Integer, ForeignKey('Readers.User_ID'))
    Staff_ID = Column(Integer, ForeignKey('Staff.Staff_ID'))
    
    book = relationship("Books")
    reader = relationship("Readers")
    staff = relationship("Staff")

class Transactions(Base):
    __tablename__ = 'Transactions'

    Transaction_ID = Column(Integer, primary_key=True, index=True)
    ReserveDate = Column(Date)
    Return_Date = Column(Date)
    Due_Date = Column(Date)
    Book_No = Column(Integer, ForeignKey('Books.Book_ID'))
    User_ID = Column(Integer, ForeignKey('Readers.User_ID'))
    
    book = relationship("Books")
    reader = relationship("Readers")

    