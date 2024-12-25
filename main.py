from fastapi import FastAPI
import models
from database import engine
from routers import authentication,librarians,student,books,issues


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(librarians.router)
app.include_router(student.router)
app.include_router(books.router)
app.include_router(issues.router)
