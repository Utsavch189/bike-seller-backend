from pydantic import BaseModel,constr,validator,ValidationError
from datetime import datetime
import base64

class BikeImageDTO(BaseModel):
    image_name:constr(strip_whitespace=True)=""
    image_b64:constr(strip_whitespace=True)=""

    @validator('image_name',allow_reuse=True,always=True)
    def check_imageALrteadyExists(cls,value):
        try:
            if value:
                value_array=value.split('.')
                image_name=value_array[0]+f'{int(datetime.timestamp(datetime.now()))}'+'.'+value_array[1]
                return image_name
            return ""
        except Exception as e:
            raise Exception(str(e))
    
    @validator('image_b64',allow_reuse=True,always=True)
    def b64_decode(cls,value):
        try:
            if value:
                if len(value.split(','))>1:
                    return base64.b64decode(value.split(',')[1])
                else:
                    return base64.b64decode(value)
            return ""
        except Exception as e:
            raise Exception(str(e))


