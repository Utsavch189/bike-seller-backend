from pydantic import BaseModel,constr,validator,ValidationError
from src.admins.models import BikeImages
import base64

class BikeImageDTO(BaseModel):
    image_name:constr(max_length=100,strip_whitespace=True)=""
    image_b64:constr(strip_whitespace=True)=""

    @validator('image_name',allow_reuse=True,always=True)
    def check_imageALrteadyExists(cls,value):
        try:
            if value:
                if BikeImages.objects.filter(image_name=value).exists():
                    raise Exception("already same image name exists!")
                return value
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