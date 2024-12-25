from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(librarians.router)
app.include_router(students.router)
app.include_router(books.router)
app.include_router(issues.router)