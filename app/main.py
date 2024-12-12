from fastapi import FastAPI
from crouton import SQLAlchemyCRUDRouter
from .database import engine, Base, get_db
from .models import Book as BookModel
from .schemas import Book, BookCreate

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Crouton Router for Book resourcer
router = SQLAlchemyCRUDRouter(
    schema=Book,
    create_schema=BookCreate,
    db_model=BookModel,
    db=get_db,
    prefix='books'
)
app.include_router(router)

# Define root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD application. Go to /docs for API documentation."}
