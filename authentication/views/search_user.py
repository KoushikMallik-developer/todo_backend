from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.export_types.request_data_types.search_user import (
    SearchUserRequestType,
)
from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.handlers.logged_in_handler import is_logged_in
from authentication.services.user_services.user_services import UserServices


class SearchUsersView(APIView):
    renderer_classes = [JSONRenderer]

    @handle_exceptions
    @is_logged_in
    def post(self, request):
        search_users = UserServices.get_searched_users(
            request_data=SearchUserRequestType(**request.data),
            uid=request.user.id,
        )
        return Response(
            data={
                "data": (search_users if search_users else []),
                "message": (
                    "Search results fetched successfully"
                    if search_users
                    else "No result found"
                ),
            },
            status=status.HTTP_200_OK,
            content_type="application/json",
        )
