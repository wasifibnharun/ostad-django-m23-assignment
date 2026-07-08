# Book Store REST API

A simple Book Store REST API built using Django REST Framework (DRF) with token authentication, filtering, searching, ordering, pagination, and throttling.

## Project Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-github-repo-url>
   cd book-store
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:** `.\venv\Scripts\activate`
   - **Mac/Linux:** `source venv/bin/activate`

4. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

## Required Packages
- `django`
- `djangorestframework`
- `django-filter`

## How to Run the Project
Start the Django development server:
```bash
python manage.py runserver
```
The API will be accessible at `http://127.0.0.1:8000/`.

## API Endpoint List

### Authentication
- **Register a new user:** `POST /api/register/`
- **Login (Get Token):** `POST /api/login/`

### Books CRUD (Token Authentication required for modifying data)
- **Retrieve all books:** `GET /api/books/` (Public)
- **Create a new book:** `POST /api/books/` (Requires Auth)
- **Retrieve a single book:** `GET /api/books/<id>/` (Public)
- **Update a book:** `PUT /api/books/<id>/` (Requires Auth)
- **Partially update a book:** `PATCH /api/books/<id>/` (Requires Auth)
- **Delete a book:** `DELETE /api/books/<id>/` (Requires Auth)

### Filtering, Searching, Ordering & Pagination (Append to GET /api/books/)
- **Filter by Author:** `?author=<name>` (e.g., `?author=J.K. Rowling`)
- **Search by Title:** `?search=<term>` (e.g., `?search=Harry`)
- **Order by Price:** `?ordering=price` (ascending) or `?ordering=-price` (descending)
- **Pagination:** `?page=<number>` (e.g., `?page=2`)

## Throttling Limits
- **Anonymous Users:** 20 requests per minute
- **Authenticated Users:** 50 requests per minute

## Postman Collection
A Postman collection containing all the necessary requests (Register, Login, and Book CRUD APIs) is included in the root folder of this project. You can import this `.json` file directly into Postman to test the endpoints.
