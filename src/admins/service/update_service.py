from src.admins.dto.updateDto.bike_dto import UpdateBikeDTO
from src.admins.dto.updateDto.bikemeta_dto import UpdateBikeMetaDTO
from django.db import transaction
from src.admins.models import Bike,BikeMeta,BikeImages
from core.utils.file_handel.main import FileHandel
from rest_framework import status
from src.customer.serializer.bike_serializer import BikeSerializer
import json

class UpdateBikeService:

    def __updateBike(self,dto:UpdateBikeDTO)->Bike:
        bike=Bike.objects.get(bike_model_id=dto.bike_model_id)

        if dto.image_name=="" and dto.image_path=="" and bike.image_path!="":
            #user deletes bike's profile image
            dto.image_path=FileHandel.delete(bike.image_path)
            
        elif dto.image_name and dto.image_path=="" and dto.image_b64:
            #user changes bike's profile image
            dto.image_path=FileHandel.write(filename=dto.image_name,decoded_data=dto.image_b64,subdir=dto.bike_model)
    
        
        bike.bike_model=dto.bike_model
        bike.brand_name=dto.brand_name
        bike.bike_name=dto.bike_name
        bike.image_path=dto.image_path
        bike.image_name=dto.image_name

        return bike
    
    def __updateBikeMeta(self,dto:UpdateBikeMetaDTO)->BikeMeta:
        bikemeta=BikeMeta.objects.get(bikemeta_id=dto.bikemeta_id)
        
        bikemeta.asking_price=dto.asking_price
        bikemeta.year_of_model=dto.year_of_model
        bikemeta.engine_cc=dto.engine_cc
        bikemeta.engine_type=dto.engine_type
        bikemeta.kms_run=dto.kms_run
        bikemeta.no_of_owners=dto.no_of_owners
        bikemeta.available=dto.available
        bikemeta.mileage=dto.mileage
        bikemeta.buy_year=dto.buy_year
        bikemeta.color=dto.color
        bikemeta.details=dto.details
        bikemeta.latest_upload=dto.latest_upload

        return bikemeta


    def __deletebikeImages(self,data:dict)->None:
        """
            data schema should be like,
                {
                    "bikeimage_id": "cb787431-a2db-11ee-a414-18c04d5465c7",
                    "image_name": "pp.png",
                    "image_path": "/media/abc/pp.png",
                    "bike": "cb762a83-a2db-11ee-a79c-18c04d5465c7"
                }
        """
        FileHandel.delete(path=data.get('image_path'))
        BikeImages.objects.filter(bikeimage_id=data.get('bikeimage_id')).delete()

    @transaction.atomic()
    def update(self,data)->tuple:
        try:
            bike_meta_data=data.pop('bike_meta')[0]
            bike_image_data=data.pop('bike_image')

            
            bikedto=UpdateBikeDTO(**data)
            bikemetadto=UpdateBikeMetaDTO(**bike_meta_data)

            bike_image_in_db=(json.loads(json.dumps(BikeSerializer(instance=Bike.objects.get(bike_model_id=bikedto.bike_model_id)).data)))['bike_image']

            bike_instance=self.__updateBike(dto=bikedto)
            bike_instance.save()

            bikemeta_instance=self.__updateBikeMeta(dto=bikemetadto)
            bikemeta_instance.save()

            image_should_be_deleted=[x for x in bike_image_in_db if x not in bike_image_data]

            for i in image_should_be_deleted:
                self.__deletebikeImages(i)
            
            return (
                {"message":"successfully updated!","bike":BikeSerializer(instance=bike_instance).data},
                status.HTTP_202_ACCEPTED
            )

        except Exception as e:
            raise Exception(str(e))