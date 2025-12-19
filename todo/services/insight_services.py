from django.db.models import Count, Q, F
from django.db.models.functions import TruncDate, ExtractHour

from todo.models import Todo


class InsightServices:
    def __init__(self):
        pass

    @staticmethod
    def get_last_fully_completed_todo_date(user_id):
        completed_dates = (
            Todo.objects.filter(user__id=user_id)
            .annotate(todo_date=TruncDate("created_at"))
            .values("todo_date")
            .annotate(
                total=Count("id"), completed=Count("id", filter=Q(completed=True))
            )
            .filter(total=F("completed"))
            .order_by("-todo_date")
        )

        return completed_dates[0]["todo_date"] if len(completed_dates) > 0 else None

    @staticmethod
    def get_overall_peak_completion_hour(user_id):
        todo = (
            Todo.objects.filter(
                user__id=user_id, completed=True, completed_at__isnull=False
            )
            .annotate(hour=ExtractHour("completed_at"))
            .values("hour")
            .annotate(cnt=Count("id"))
            .order_by("-cnt")
            .first()
        )
        return todo["hour"] if todo else None

    @staticmethod
    def get_average_daily_completion(user_id):
        daily_counts = (
            Todo.objects.filter(
                user__id=user_id, completed=True, completed_at__isnull=False
            )
            .annotate(day=TruncDate("completed_at"))
            .values("day")
            .annotate(completed_count=Count("id"))
        )

        if not daily_counts:
            return 0

        total_completed = sum(d["completed_count"] for d in daily_counts)
        active_days = len(daily_counts)

        return round(total_completed / active_days, 2)
