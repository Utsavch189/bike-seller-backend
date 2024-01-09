from rest_framework.views import APIView
from core.utils.responses.response import Response
from core.utils.decorator.handelException import handel_exception
from core.utils.decorator.logger import log
from src.customer.service.get_service import GetBikeService

import logging,re

logger=logging.getLogger('mylogger')

class GetBikeViews(APIView):

    @handel_exception
    @log(logger=logger)
    def get(self,request)->Response:
        QUERY_STRING=request.META.get('QUERY_STRING')
        if QUERY_STRING:
            res=re.split(r'[?&/]',QUERY_STRING)
            if res[len(res)-1]=='':
                res.pop()
            query_dict={key_value.split('=')[0]: key_value.split('=')[1].rstrip('/') for key_value in res}
        else:
            query_dict=None
        message,status=GetBikeService().get(query=query_dict)
        return Response(data=message,status=status)