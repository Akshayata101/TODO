from pydantic import BaseModel
class Todo(BaseModel):
    id:int
    task:str
    describe:str
    status:bool= False
