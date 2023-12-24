from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str

tasks = []

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    tasks.append(task.dict())
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task['id'] == task_id:
            task.update(updated_task.dict())
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            del tasks[i]
            return task
    raise HTTPException(status_code=404, detail="Task not found")
