from src.admins.models import Bike,BikeImages
from src.admins.dto.mainDto.bikeimages_dto import BikeImageDTO
from rest_framework import status
from core.utils.threads.main import Thread
from src.admins.service.upload_service import UploadBikeService
from src.customer.serializer.bike_serializer import BikeSerializer

class UploadImageService:

    def upload(self,data:dict,model_id:str)->tuple:
        try:
            """
                {
                    "bike_image":[
                        {"image_name":"","image_b64":""},
                    ]
                }
            """
            bike=Bike.objects.get(bike_model_id=model_id)
            bike_image_data=data.pop('bike_image')
            threads=[]
            service=UploadBikeService()
            for i in bike_image_data:
                t=Thread(target=service.createBikeImages,args=(bike,BikeImageDTO(**i)))
                t.start()
                threads.append(t)
            for thread in threads:
                res=thread.join()
                res.save()
            return ({
                "message":"bike images are created!",
                "bike":BikeSerializer(instance=bike).data
            },status.HTTP_201_CREATED)

        except Exception as e:
            raise Exception(str(e))