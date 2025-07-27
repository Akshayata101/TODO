# FastAPI TODO API

This is a simple TODO list API built with FastAPI. It demonstrates basic CRUD operations (Create, Read, Update, Delete) using Python's modern asynchronous web framework.

## Features

- Retrieve all TODO items
- Retrieve a specific TODO item by ID
- Add a new TODO item
- Update an existing TODO item
- Delete a TODO item

## Tech Stack

- FastAPI for building the web API
- Pydantic for data validation and serialization
- Uvicorn as the ASGI server

## API Endpoints

- `GET /` – Returns a welcome message
- `GET /todos` – Returns a list of all TODO items
- `GET /todos/{id}` – Returns a specific TODO item
- `POST /todos` – Adds a new TODO item
- `PUT /todos/{id}` – Updates an existing TODO item
- `DELETE /todos/{id}` – Deletes a TODO item

## Sample Request (POST or PUT)

```json
{
  "id": 1,
  "title": "Learn FastAPI with TODO list",
  "description": "Fist TODO then tudumm",
  "completed": true
}

