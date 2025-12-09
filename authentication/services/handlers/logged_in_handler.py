from functools import wraps

from rest_framework_simplejwt.exceptions import TokenError

from authentication.services.handlers.exeption_handler_decorator import (
    handle_exceptions,
)
from authentication.services.helpers import decode_jwt_token, validate_user_uid


@handle_exceptions
def is_logged_in(view_func):
    @wraps(view_func)
    def _wrapped_view(*args, **kwargs):
        request = args[1]
        user_id = decode_jwt_token(request=request)
        if validate_user_uid(uid=user_id).is_validated:
            request.user.id = user_id
            return view_func(*args, **kwargs)
        else:
            raise TokenError()

    return _wrapped_view
