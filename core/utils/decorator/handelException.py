from rest_framework.response import Response
from datetime import datetime
from rest_framework import status
from pydantic import ValidationError

def handel_exception(func):
    
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
             if (type(e)==ValidationError):
                _error={}
                for i in e.errors():
                    replacement = i['loc'][0]
                    s = i['msg'].split()
                    s[0] = replacement
                    _error[i['loc'][0]]=' '.join(s)
                return Response({"message":_error,"timestamp":datetime.timestamp(datetime.now())},status=status.HTTP_400_BAD_REQUEST)
                
             return Response({"message":str(e),"timestamp":datetime.timestamp(datetime.now())},status=status.HTTP_400_BAD_REQUEST)
    return inner