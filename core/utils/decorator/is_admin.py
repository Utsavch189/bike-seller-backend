from rest_framework.response import Response
from rest_framework import status

def isAdmin(func):
    def inner(request,*args, **kwargs):
        if request.user.user_type=='admin':
            return func(request,*args, **kwargs)
        else:
            return Response({"message":"permission denied!"},status=status.HTTP_401_UNAUTHORIZED)
    return inner