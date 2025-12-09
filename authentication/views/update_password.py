from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.export_types.request_data_types.change_password import (
    ChangePasswordRequestType,
)
from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.handlers.logged_in_handler import is_logged_in
from authentication.services.user_services.user_services import UserServices


class UpdatePasswordView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    @is_logged_in
    def post(self, request):
        UserServices().change_password(
            uid=request.user.id, request_data=ChangePasswordRequestType(**request.data)
        )
        return Response(
            data={
                "message": "Password updated successfully.",
            },
            status=status.HTTP_200_OK,
            content_type="application/json",
        )
