from core.utils.decorator.is_admin import isAdmin
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from core.utils.responses.response import Response
from core.utils.decorator.handelException import handel_exception
from core.utils.decorator.logger import log
from rest_framework import status
import logging
from src.admins.models import Bike

logger=logging.getLogger('mylogger')

class DeleteViews(APIView):

    authentication_classes=[SessionAuthentication,TokenAuthentication]
    permission_classes=[IsAuthenticated]

    @handel_exception
    @log(logger=logger)
    @isAdmin
    def delete(self,request):
        if not request.data.get('model_id'):
            raise Exception('model_id required!')
        Bike.objects.filter(bike_model_id=request.data.get('model_id')).delete()
        return Response({"message":"successfully deleted!"},status=status.HTTP_202_ACCEPTED)