from fastapi import FastAPI,HTTPException
from models import Todo

app=FastAPI()

todos=[]

@app.get("/")
def home():
    return {"message":"Welcome to TODO: first todo then tudumm"}

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.post("/todos")
def add_todo(todo: Todo):
    for existing in todos:
        if existing.id == todo.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    todos.append(todo)
    return {"message": "Todo added", "todo": todo}


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {"message": "Todo updated", "todo": updated_todo}
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
