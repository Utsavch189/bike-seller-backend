from rest_framework.views import APIView
from core.utils.responses.response import Response
from core.utils.decorator.handelException import handel_exception
from core.utils.decorator.logger import log
from src.admins.service.upload_service import UploadBikeService
from core.utils.decorator.is_admin import isAdmin

from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

import logging

logger=logging.getLogger('mylogger')

class UploadBikeViews(APIView):

    authentication_classes=[SessionAuthentication,TokenAuthentication]
    permission_classes=[IsAuthenticated]

    @handel_exception
    @log(logger=logger)
    @isAdmin
    def post(self,request)->Response:
        message,status=UploadBikeService().upload(data=request.data)
        return Response(data=message,status=status)