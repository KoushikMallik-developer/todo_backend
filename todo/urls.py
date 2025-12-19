from django.urls import path

from todo.views.all_todos import AllTodosView
from todo.views.create_todo import CreateTodoView
from todo.views.delete_todo import DeleteTodoView
from todo.views.fetch_todo_for_date import FetchTodosForDateView
from todo.views.insights import InsightsTodosView
from todo.views.stats import StatsTodosView
from todo.views.toggle_todo import ToggleTodoCompletionView
from todo.views.update_todo import UpdateTodoView

urlpatterns = [
    path("all", AllTodosView.as_view(), name="all_todos"),
    path("create", CreateTodoView.as_view(), name="all_todos"),
    path("delete", DeleteTodoView.as_view(), name="all_todos"),
    path("update", UpdateTodoView.as_view(), name="all_todos"),
    path("toggle", ToggleTodoCompletionView.as_view(), name="all_todos"),
    path("fetch-for-date", FetchTodosForDateView.as_view(), name="date_todos"),
    path("stats", StatsTodosView.as_view(), name="stats_todos"),
    path("insights", InsightsTodosView.as_view(), name="user_insights"),
]
