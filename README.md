Flask API for User Authentication and Resource Management
Project Description

This project is a Flask-based API implementing user authentication and resource management. Users can register, log in, and create, update, delete, and retrieve their personal entries. The API supports session-based authentication, pagination, and secure access control.

Installation Instructions
Requirements
Ensure you have:
- Python 3.8+
- Pipenv
- SQLite (or PostgreSQL for production)
- Flask and necessary extensions

Setup
- Clone the repository:
git clone <repository-url>
cd flask-api
pipenv install
pipenv shell
- Set up the database:
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python seed.py
- Run the application:
python app.py


API Endpoints
Authentication
- POST /auth/register – Register a user
- POST /auth/login – Log in

Resource Management
- GET /api/entries?page=<int>&per_page=<int> – Retrieve entries
- POST /api/entries – Create an entry
- PATCH /api/entries/<id> – Update an entry
- DELETE /api/entries/<id> – Delete an entry

Testing
Run tests with:
pytest tests


Security Considerations
- Passwords are hashed using Flask-Bcrypt.
- Users can only access their own data.
- Sessions are used for authentication.
