from rest_framework.authtoken.models import Token
from src.auths.dto.login_dto import LoginDTO
from rest_framework import status
from src.auths.serializers import UserSerializer

class LoginService:
    
    def __init__(self,dto:LoginDTO) -> None:
        self.dto=dto

    def login(self)->tuple:
        try:
            user=self.dto.username
            token,created=Token.objects.get_or_create(user=user)
            message={
                "message":"logged in!",
                "token":token.key,
                "created":created,
                "user":UserSerializer(instance=user).data
            }
            return (message,status.HTTP_200_OK)
        except Exception as e:
            raise Exception(str(e))