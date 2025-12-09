from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ExportTodo(BaseModel):
    id: Optional[UUID]
    title: str
    user: Optional[UUID]
    completed: bool

    def __init__(self, **kwargs):
        if kwargs.get("user") and hasattr(kwargs["user"], "username"):
            kwargs["user"] = kwargs["user"].id
        super().__init__(**kwargs)


class ExportTodoList(BaseModel):
    todos: list[ExportTodo]
