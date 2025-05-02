
from rest_framework import authentication, exceptions

from .models import User

class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        request.user = None

        auth_header = authentication.get_authorization_header(request).split()


        print (auth_header)

        if not auth_header:
            return None
        
        if len(auth_header) != 2:
            return None
        

        username = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        try:
            int(token)
    
            if str(len(token)) > 6:
                msg = 'Токен должен быт 6-и значным числом'
                raise exceptions.AuthenticationFailed(msg)

        except ValueError:
            msg = 'Токен должен быт 6-и значным числом'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        return self._authenticate_credentials(request, user, token)
    

    def _authenticate_credentials(self, request, user, token):
        

        if not user.token_isvalid(token):
            msg = 'Неверный токен'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = 'Данный пользователь деактивирован.'
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)