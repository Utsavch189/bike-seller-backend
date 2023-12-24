from rest_framework.response import Response
from rest_framework.views import APIView
from src.auths.dto.login_dto import LoginDTO
from src.auths.service.login_service import LoginService
from core.utils.decorator.handelException import handel_exception
from core.utils.decorator.logger import log

import logging

logger=logging.getLogger('mylogger')

class LoginView(APIView):

    @handel_exception
    @log(logger=logger)
    def post(self,request)->Response:
        login_service=LoginService(dto=LoginDTO(**request.data))
        message,status=login_service.login()
        return Response(data=message,status=status)
