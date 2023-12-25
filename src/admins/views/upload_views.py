from rest_framework.views import APIView
from rest_framework.response import Response
from core.utils.decorator.handelException import handel_exception
from core.utils.decorator.logger import log
from src.admins.service.upload_service import UploadBikeService

import logging

logger=logging.getLogger('mylogger')

class UploadBikeViews(APIView):

    @handel_exception
    @log(logger=logger)
    def post(self,request)->Response:
        message,status=UploadBikeService().upload(data=request.data)
        return Response(data=message,status=status)