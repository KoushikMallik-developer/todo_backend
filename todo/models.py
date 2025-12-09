from django.db import models

from authentication.models.base_models.base_model import GenericBaseModel
from authentication.models.user_models.user import User


class Todo(GenericBaseModel):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
