Cafe & Wifi API

A custom, fully functional REST API built with Python, Flask, and SQLAlchemy.It simulates a backend database system for managing cafes, their locations, and amenities.

Features

This API supports full CRUD (Create, Read, Update, Delete) operations using RESTful routing architecture:
- GET: Fetch a random cafe, or view all cafes currently in the database.
- GET: Search for cafes in a specific location.
- POST: Add a new cafe with details like Wi-Fi availability, socket access, and pricing.
- PATCH: Update the coffee price for a specific cafe.
- DELETE: Remove a cafe from the database (requires a secret API authentication key).

Tech Stack

- Backend Framework: Python (Flask)
- Database: SQLite & Flask-SQLAlchemy
- Data Format: JSON
- Testing & Documentation: Postman
