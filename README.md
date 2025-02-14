# Tech_Foring
# Project API

This project is a Django-based application that provides an API for managing users, projects, tasks, and comments. It uses Django REST Framework (DRF) for creating and managing the API endpoints and `drf-yasg` for automatic Swagger API documentation.

## Prerequisites

Before setting up the project, ensure you have the following installed:
- Python 3.x (preferably Python 3.8 or later)
- pip (Python package manager)
- Django 3.x or later
- Django REST Framework
- drf-yasg for Swagger documentation

## Setup Instructions

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

First, clone the repository to your local machine:
```bash
git clone https://github.com/AbuZaferMdFahim/Tech_Foring.git
cd project-api

# Create a virtual environment (replace 'venv' with your preferred environment name)
python3 -m venv venv

# Activate the virtual environment
# On Windows
env\Scripts\activate
# On macOS/Linux
source venv/bin/activate

pip install -r requirements.txt


# Apply migrations to the database
python manage.py migrate

python manage.py createsuperuser
python manage.py runserver

# Access Swagger UI (API Documentation)
# Once the server is running, you can access the Swagger-based API documentation via the following URL:

Swagger UI: http://localhost:8000/api/swagger/


# API Endpoints
# Here’s a brief overview of the available endpoints:

# Users
POST /api/users/register/: Register a new user
POST /api/users/login/: Authenticate a user and return a token
GET /api/users/{id}/: Retrieve user details
PUT/PATCH /api/users/{id}/: Update user details
DELETE /api/users/{id}/: Delete a user account

# Projects
GET /api/projects/: List all projects
POST /api/projects/: Create a new project
GET /api/projects/{id}/: Retrieve project details
PUT/PATCH /api/projects/{id}/: Update project details
DELETE /api/projects/{id}/: Delete a project

# Tasks
GET /api/projects/{project_id}/tasks/: List all tasks in a project
POST /api/projects/{project_id}/tasks/: Create a new task in a project
GET /api/tasks/{id}/: Retrieve task details
PUT/PATCH /api/tasks/{id}/: Update task details
DELETE /api/tasks/{id}/: Delete a task

# Comments
GET /api/tasks/{task_id}/comments/: List all comments on a task
POST /api/tasks/{task_id}/comments/: Create a new comment on a task
GET /api/comments/{id}/: Retrieve comment details
PUT/PATCH /api/comments/{id}/: Update comment details
DELETE /api/comments/{id}/: Delete a comment