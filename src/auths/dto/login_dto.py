from pydantic import BaseModel,validator,constr
from django.contrib.auth import get_user_model

User=get_user_model()

class LoginDTO(BaseModel):
    username:constr(min_length=1,max_length=100,strip_whitespace=True)
    password:constr(min_length=1,max_length=15,strip_whitespace=True)

    @validator('username',allow_reuse=True,always=True)
    def check_username(cls,value):
        try:
            if not User.objects.filter(username=value).exists():
                raise Exception("user doesn't exists!")
            
            return User.objects.get(username=value)

        except Exception as e:
            raise Exception(str(e))
    
    @validator('password',allow_reuse=True,always=True)
    def check_password(cls,value,values):
        try:
            if not values['username'].check_password(value):
                raise Exception("password is wrong!")
            
            return value

        except Exception as e:
            raise Exception(str(e))