from django.urls import path

from todo_backend.views.all_todos import AllTodosView
from todo_backend.views.create_todo import CreateTodoView
from todo_backend.views.delete_todo import DeleteTodoView
from todo_backend.views.toggle_todo import ToggleTodoCompletionView
from todo_backend.views.update_todo import UpdateTodoView

urlpatterns = [
    path("dashboard", AllTodosView.as_view(), name="all_todos"),
    path("create", CreateTodoView.as_view(), name="all_todos"),
    path("delete", DeleteTodoView.as_view(), name="all_todos"),
    path("update", UpdateTodoView.as_view(), name="all_todos"),
    path("toggle", ToggleTodoCompletionView.as_view(), name="all_todos"),
]
