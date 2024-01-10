from django.db import transaction
from src.admins.models import Bike,BikeMeta,BikeImages
from core.utils.file_handel.main import FileHandel
from rest_framework import status
from src.customer.serializer.bike_serializer import BikeSerializer
import uuid
from django.utils import timezone
from src.admins.dto.mainDto.bike_dto import BikeDTO
from src.admins.dto.mainDto.bikemeta_dto import BikeMetaDTO
from src.admins.dto.mainDto.bikeimages_dto import BikeImageDTO


class UploadBikeService:
    
    def __createBikeMeta(self,bike:Bike,dto:BikeMetaDTO)->BikeMeta:
    
        bikemeta=BikeMeta(
            bikemeta_id=uuid.uuid1(),
            bike=bike,
            asking_price=dto.asking_price,
            year_of_model=dto.year_of_model,
            engine_cc=dto.engine_cc,
            engine_type=dto.engine_type,
            kms_run=dto.kms_run,
            no_of_owners=dto.no_of_owners,
            available=dto.available,
            mileage=dto.mileage,
            buy_year=dto.buy_year,
            color=dto.color,
            details=dto.details,
            latest_upload=timezone.now()
        )
        return bikemeta

    def createBikeImages(self,bike:Bike,dto:BikeImageDTO)->BikeImages:

        if BikeImages.objects.filter(image_name=dto.image_name).exists():
            raise Exception("already same image name exists!")

        _image_path=FileHandel.write(filename=dto.image_name,decoded_data=dto.image_b64,subdir=bike.bike_model)

        bikeimage=BikeImages(
            bikeimage_id=uuid.uuid1(),
            bike=bike,
            image_path=_image_path,
            image_name=dto.image_name
        )
        return bikeimage

    def __createBike(self,dto:BikeDTO)->Bike:
        if dto.image_name:
            if Bike.objects.filter(image_name=dto.image_name).exists():
                raise Exception("already same image name exists!")

            _image_path=FileHandel.write(filename=dto.image_name,decoded_data=dto.image_b64,subdir=dto.bike_model)
        else:
            _image_path=""
        
        bike=Bike(
            bike_model_id=uuid.uuid1(),
            bike_model=dto.bike_model,
            brand_name=dto.brand_name,
            bike_name=dto.bike_name,
            image_path=_image_path,
            image_name=dto.image_name
        )
        return bike
    
    @transaction.atomic()
    def upload(self,data)->tuple:
        try:
            if data.get('bike_image'):
                bike_image_data=data.pop('bike_image')
            else:
                bike_image_data=[]

            bike_meta_data=data.pop('bike_meta')
            
            bikedto=BikeDTO(**data)
            bikemetadto=BikeMetaDTO(**bike_meta_data[0])
            
            
            _bike_instace=self.__createBike(dto=bikedto)
            
    
            _bikemeta_instace=self.__createBikeMeta(bike=_bike_instace,dto=bikemetadto)
            print(_bike_instace)

            if bike_image_data:
                for i in bike_image_data:
                    bikeimage=self.createBikeImages(_bike_instace,BikeImageDTO(**i))
                    bikeimage.save()

            _bike_instace.save()
            _bikemeta_instace.save()
                
                    
            return ({
                "message":"bike info is created!",
                "bike":BikeSerializer(instance=_bike_instace).data
            },status.HTTP_201_CREATED)
            
        except Exception as e:
            print(e)
            raise Exception(str(e))