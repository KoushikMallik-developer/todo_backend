from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models.user_models.user import User
from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.handlers.logged_in_handler import is_logged_in


class RemoveUserView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    @is_logged_in
    def post(self, request):
        User.objects.get(id=request.user.id).delete()
        return Response(
            data={
                "message": "User removed Successfully.",
            },
            status=status.HTTP_200_OK,
            content_type="application/json",
        )
