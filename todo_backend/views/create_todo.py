from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models.user_models.user import User
from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.handlers.logged_in_handler import is_logged_in
from todo.export_types.export_todo import ExportTodo
from todo.models import Todo


class CreateTodoView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    @is_logged_in
    def post(self, request):
        title = request.data.get("title")
        if not title:
            raise ValueError("Title is required.")
        user = User.objects.get(id=request.user.id)
        todo = Todo.objects.create(title=title, user=user)
        export_todo = ExportTodo(**todo.model_to_dict())
        return Response(
            data={
                "message": "Todo created successfully.",
                "data": export_todo.model_dump(),
            },
            status=201,
            content_type="application/json",
        )
