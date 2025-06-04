from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken, TokenError

def jwt_exception(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, NotAuthenticated):
            response.data['detail'] = 'token_expired'
        elif isinstance(exc, AuthenticationFailed):
            response.data['detail'] = 'invalid_token'
        elif isinstance(exc, (TokenError, InvalidToken)):
            response.data['detail'] = 'invalid_or_expired_token'

    return response