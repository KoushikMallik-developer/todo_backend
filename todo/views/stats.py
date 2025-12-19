from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.handlers.logged_in_handler import is_logged_in
from todo.models import Todo
from todo.services.insight_services import InsightServices


class StatsTodosView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    @is_logged_in
    def get(self, request):
        total_todos_count = Todo.objects.filter(user__id=request.user.id).count()
        completed_todos_count = Todo.objects.filter(
            user__id=request.user.id, completed=True
        ).count()
        completion_rate = (
            (completed_todos_count / total_todos_count) * 100
            if total_todos_count > 0
            else 0
        )

        stats = {
            "total_todos_count": total_todos_count,
            "completed_todos_count": completed_todos_count,
            "completion_rate": f"{completion_rate:.2f}",
            "average_completion_per_day": InsightServices().get_average_daily_completion(
                request.user.id
            ),
        }
        return Response(
            data={
                "message": "Stats fetched successfully.",
                "data": stats,
            },
            status=200,
            content_type="application/json",
        )
