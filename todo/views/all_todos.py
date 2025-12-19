from datetime import date

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.handlers.logged_in_handler import is_logged_in
from todo.export_types.export_todo import ExportTodoList, ExportTodo
from todo.models import Todo


class AllTodosView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    @is_logged_in
    def get(self, request):
        today = date.today()
        todos = Todo.objects.filter(user__id=request.user.id, created_at__date=today)

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
