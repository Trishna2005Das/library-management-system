from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
from datetime import date

class Books(Base):
    __tablename__ = 'Books'

    Book_ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Quantity = Column(Integer)
    Author = Column(String)
    Genre = Column(String)
    PublicationYear = Column(Integer)
    ISBN = Column(String)
    
    issues=relationship("Issues",back_populates="book")

class Students(Base):
    __tablename__ = 'Students'

    Student_ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Department = Column(String)
    YearOfStudy = Column(Integer)
    ContactNumber = Column(String)
    issues=relationship("Issues",back_populates="student")

class Librarians(Base):
    __tablename__ = 'Librarians'

    Librarian_ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Designation = Column(String)
    ContactNumber = Column(String)

class Issues(Base):
    __tablename__ = 'Issues'

    Issue_ID = Column(Integer, primary_key=True, index=True)
    Student_ID = Column(Integer, ForeignKey('Students.Student_ID'))
    Book_ID = Column(Integer, ForeignKey('Books.Book_ID'))
    IssueDate = Column(date)
    DueDate = Column(date)
    ReturnDate = Column(date)
    books=relationship("Book",back_populates="issues")
    students=relationship("Student",back_populates="issues")
    Librarian_ID = Column(Integer, ForeignKey(' Librarians.Librarian_ID'))
    
#     Each relationship operates independently because:
# The issues in Book filters rows in the Issue table using book_id.
# The issues in Student filters rows in the Issue table using student_id.

# back_populates Ensures Consistency:

# back_populates ensures that the relationships are bidirectional.
# In the Issue class:
# student = relationship("Student", back_populates="issues") ties issues in Student to the student attribute in Issue.
# book = relationship("Book", back_populates="issues") ties issues in Book to the book attribute in Issue.