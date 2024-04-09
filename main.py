from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    name: str
    description: Optional[str] = None


# https://www.youtube.com/watch?v=gBfkX9H3szQ
# 09.04.24 остановился на восьмой минуте
@app.get("/tasks")
def get_tasks():
    task = Task(name="Запиши это видео")
    return {"data": task}
