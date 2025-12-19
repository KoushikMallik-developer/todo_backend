from datetime import datetime

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.handlers.logged_in_handler import is_logged_in
from todo.export_types.export_todo import ExportTodo
from todo.models import Todo


class ToggleTodoCompletionView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    @is_logged_in
    def post(self, request):
        todo_id = request.data.get("todo_id")
        if not todo_id:
            raise ValueError("Todo ID is required.")
        todo = Todo.objects.get(id=todo_id)
        if str(todo.user.id) != request.user.id:
            raise PermissionError("You do not have permission to delete this todo.")
        todo.completed = not todo.completed
        todo.completed_at = None if not todo.completed else datetime.now()
        todo.save()
        export_todo = ExportTodo(**todo.model_to_dict())
        return Response(
            data={
                "message": "Todo completion status toggled successfully.",
                "data": export_todo.model_dump(),
            },
            status=200,
            content_type="application/json",
        )
