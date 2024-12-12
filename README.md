# FastAPI CRUD Application with Crouton

This project demonstrates a simple FastAPI application that implements CRUD (Create, Read, Update, Delete) functionality for a `Book` resource using the [Crouton](https://github.com/swarmauri/crouton) library for easy database interaction. The project uses SQLAlchemy for database models and Pydantic for request/response validation.

## Features:
- **CRUD Operations** for a Book resource
- **SQLite** database for storing Book data
- **FastAPI** web framework for routing and API
- **Crouton** for automatic CRUD route generation

## Prerequisites:
- Python 3.7 or higher
- SQLite (comes with FastAPI and SQLAlchemy)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   cd yourrepo
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Access the API documentation: Go to http://127.0.0.1:8000/docs for an interactive interface where you can test the API.

# Folder Structure
 ```
/yourproject
├── /app
│   ├── /models          # SQLAlchemy database models
│   ├── /schemas         # Pydantic models for request validation
│   ├── /database        # Database connection and session management
│   ├── /main.py         # FastAPI app and CRUD routes setup
├── /requirements.txt    # Project dependencies
└── /README.md           # This README file
```
# API Endpoints:
  GET /books/ - Get a list of all books
  POST /books/ - Create a new book
  GET /books/{id}/ - Get a book by ID
  PUT /books/{id}/ - Update a book by ID
  DELETE /books/{id}/ - Delete a book by ID

## License:
This project is licensed under the MIT License.
