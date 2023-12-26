from rest_framework.views import APIView
from core.utils.decorator.handelException import handel_exception
from core.utils.decorator.logger import log
from core.utils.responses.response import Response
from src.admins.service.uploadimages_service import UploadImageService
from core.utils.decorator.is_admin import isAdmin

from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated


import logging

logger=logging.getLogger('mylogger')

class UploadImagesViews(APIView):

    authentication_classes=[SessionAuthentication,TokenAuthentication]
    permission_classes=[IsAuthenticated]

    @handel_exception
    @log(logger=logger)
    @isAdmin
    def post(self,request,model_id)->Response:
        message,status=UploadImageService().upload(data=request.data,model_id=model_id)
        return Response(data=message,status=status)