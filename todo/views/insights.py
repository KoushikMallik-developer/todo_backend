from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.handlers.logged_in_handler import is_logged_in
from todo.services.insight_services import InsightServices


class InsightsTodosView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    @is_logged_in
    def get(self, request):
        insights = {
            "last_fully_completed_todo_date": InsightServices.get_last_fully_completed_todo_date(
                request.user.id
            ),
            "average_completion_per_day": InsightServices.get_average_daily_completion(
                request.user.id
            ),
            "overall_peak_completion_hour": InsightServices.get_overall_peak_completion_hour(
                request.user.id
            ),
        }
        return Response(
            data={
                "message": "Insights fetched successfully.",
                "data": insights,
            },
            status=200,
            content_type="application/json",
        )
