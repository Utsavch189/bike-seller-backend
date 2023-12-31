from pydantic import BaseModel,constr,validator,ValidationError
from src.admins.models import Bike
from datetime import datetime
import base64

class UpdateBikeDTO(BaseModel):
    bike_model_id:constr(min_length=1,max_length=100,strip_whitespace=True)
    bike_model:constr(min_length=1,max_length=100,strip_whitespace=True)
    brand_name:constr(min_length=1,max_length=100,strip_whitespace=True)
    bike_name:constr(min_length=1,max_length=100,strip_whitespace=True)
    image_name:constr(max_length=100,strip_whitespace=True)=""
    image_b64:constr(strip_whitespace=True)=""
    image_path:constr(max_length=100,strip_whitespace=True)=""
    
    @validator('image_name',allow_reuse=True,always=True)
    def check_imageALrteadyExists(cls,value,values):
        try:
            if value:
                value_array=value.split('.')
                image_name=value_array[0]+f'{int(datetime.timestamp(datetime.now()))}'+'.'+value_array[1]
                return image_name
            return ""
        except ValidationError as e:
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
        except ValidationError as e:
            raise Exception(str(e))

