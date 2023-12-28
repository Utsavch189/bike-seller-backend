from rest_framework.views import APIView
from core.utils.responses.response import Response
from core.utils.decorator.handelException import handel_exception
from core.utils.decorator.logger import log
from src.customer.service.get_service import GetBikeService

import logging

logger=logging.getLogger('mylogger')

class GetBikeViews(APIView):

    @handel_exception
    @log(logger=logger)
    def get(self,request)->Response:
        QUERY_STRING=request.META.get('QUERY_STRING')
        print(request.META.get('PATH_INFO'))
        if QUERY_STRING:
            QUERY_STRING_LIST=QUERY_STRING.split('?')
            QUERY_STRING_LIST[len(QUERY_STRING_LIST)-1]=QUERY_STRING_LIST[len(QUERY_STRING_LIST)-1].split('/')[0]
            QUERY_STRING_DICT = {key_value.split('=')[0]: key_value.split('=')[1].rstrip('/') for key_value in QUERY_STRING_LIST}
        else:
            QUERY_STRING_DICT=None
        message,status=GetBikeService().get(query=QUERY_STRING_DICT)
        return Response(data=message,status=status)