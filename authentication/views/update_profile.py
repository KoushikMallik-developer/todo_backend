from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.export_types.request_data_types.update_user_profile import (
    UpdateUserProfileRequestType,
)
from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.handlers.logged_in_handler import is_logged_in
from authentication.services.user_services.user_services import UserServices


class UpdateProfileView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    @is_logged_in
    def post(self, request):
        user = UserServices().update_user_profile(
            uid=request.user.id,
            request_data=UpdateUserProfileRequestType(**request.data),
        )
        return Response(
            data={
                "message": "User details updated Successfully.",
                "data": user.model_dump(),
            },
            status=status.HTTP_200_OK,
            content_type="application/json",
        )
