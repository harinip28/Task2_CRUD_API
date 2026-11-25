# Task CRUD API

## Project Overview
This project is a Task Management REST API developed using Django REST Framework.

It allows users to register, log in, create tasks, view tasks, update tasks, and delete tasks.

## Technologies Used
- Python
- Django
- Django REST Framework
- SQLite
- Postman

## Features
1. User Registration
2. User Login
3. Token Authentication
4. Create Task
5. Read Task
6. Update Task
7. Delete Task

## API Endpoints

| Method | Endpoint | Operation |
|---|---|---|
| POST | /api/register/ | Register |
| POST | /api/login/ | Login |
| GET | /api/tasks/ | View Tasks |
| POST | /api/tasks/ | Create Task |
| PUT | /api/tasks/2/ | Update Task |
| DELETE | /api/tasks/2/ | Delete Task |

## Authentication

The project uses Token Authentication.

Add the following header to authenticated requests:

Authorization: Token YOUR_TOKEN

## Testing

All CRUD operations were tested using Postman.

## Project Status

Successfully implemented CREATE, READ, UPDATE and DELETE operations.