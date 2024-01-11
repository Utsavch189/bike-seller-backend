from core.utils.decorator.is_admin import isAdmin
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from core.utils.responses.response import Response
from core.utils.decorator.handelException import handel_exception
from core.utils.decorator.logger import log
import logging
from src.admins.service.delete_service import DeleteBikeService

logger=logging.getLogger('mylogger')

class DeleteViews(APIView):

    authentication_classes=[SessionAuthentication,TokenAuthentication]
    permission_classes=[IsAuthenticated]

    @handel_exception
    @log(logger=logger)
    @isAdmin
    def delete(self,request):
        message,status=DeleteBikeService.delete(request.data.get('model_id'))
        return Response(message,status)