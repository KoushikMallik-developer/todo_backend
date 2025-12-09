from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.handlers.logged_in_handler import is_logged_in
from authentication.services.user_services.user_services import UserServices


class UserDetailView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    @is_logged_in
    def get(self, request):
        user_details = UserServices().get_user_details(uid=request.user.id)
        return Response(
            data={
                "message": "User details fetched successfully.",
                "data": user_details.model_dump(),
            },
            status=status.HTTP_200_OK,
            content_type="application/json",
        )
