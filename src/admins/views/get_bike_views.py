from rest_framework.views import APIView
from rest_framework.response import Response
from core.utils.decorator.handelException import handel_exception
from core.utils.decorator.logger import log
from src.admins.service.get_bike_service import GetBikeService

import logging

logger=logging.getLogger('mylogger')

class GetBikeViews(APIView):

    @handel_exception
    @log(logger=logger)
    def get(self,request,model_id:str)->Response:
        message,status=GetBikeService().get(model_id=model_id)
        return Response(data=message,status=status)