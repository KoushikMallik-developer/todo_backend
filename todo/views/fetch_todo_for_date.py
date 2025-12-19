from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.handlers.logged_in_handler import is_logged_in
from authentication.services.helpers import string_to_datetime
from todo.export_types.export_todo import ExportTodoList, ExportTodo
from todo.models import Todo


class FetchTodosForDateView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    @is_logged_in
    def get(self, request):
        todo_date = request.data.get("todo_date")
        if not todo_date:
            raise ValueError("Date is required.")
        day = string_to_datetime(todo_date).date()
        todos = Todo.objects.filter(user__id=request.user.id, created_at__date=day)
        export_todos_list: ExportTodoList = ExportTodoList(
            todos=[ExportTodo(**todo.model_to_dict()) for todo in todos]
        )
        todos = export_todos_list.model_dump().get("todos")
        return Response(
            data={
                "message": "Todos fetched successfully.",
                "data": todos,
            },
            status=200,
            content_type="application/json",
        )
