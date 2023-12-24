from django.db import transaction
from src.admins.models import Bike,BikeMeta,BikeImages
from core.utils.file_write.main import FileWrite
from core.utils.threads.main import Thread
from rest_framework import status
from src.admins.serializer.bike_serializer import BikeSerializer
import uuid
from django.utils import timezone



class UploadBikeService:
    
    def __createBikeMeta(self,bike:Bike,data:dict)->BikeMeta:
    

        bikemeta=BikeMeta(
            bikemeta_id=uuid.uuid1(),
            bike=bike,
            asking_price=data['asking_price'],
            year_of_model=data['year_of_model'],
            engine_cc=data['engine_cc'],
            engine_type=data['engine_type'],
            kms_run=data['kms_run'],
            no_of_owners=data['no_of_owners'],
            available=data['available'],
            mileage=data['mileage'],
            buy_year=data['buy_year'],
            color=data['color'],
            details=data['details'],
            latest_upload=timezone.now()
        )
        return bikemeta

    def createBikeImages(self,bike:Bike,data:dict)->BikeImages:

        if BikeImages.objects.filter(image_name=data['image_name']).exists():
            raise Exception("already same image name exists!")

        _image_path=FileWrite.write(filename=data['image_name'],decoded_data=data['image_b64'],subdir=bike.bike_model)

        bikeimage=BikeImages(
            bikeimage_id=uuid.uuid1(),
            bike=bike,
            image_path=_image_path,
            image_name=data['image_name']
        )
        return bikeimage

    def __createBike(self,data)->Bike:

        if Bike.objects.filter(image_name=data['image_name']).exists():
            raise Exception("already same image name exists!")

        _image_path=FileWrite.write(filename=data['image_name'],decoded_data=data['image_b64'],subdir=data['bike_model'])
        
        bike=Bike(
            bike_model_id=uuid.uuid1(),
            bike_model=data['bike_model'],
            brand_name=data['brand_name'],
            bike_name=data['bike_name'],
            image_path=_image_path,
            image_name=data['image_name']
        )

        return bike
    
    @transaction.atomic()
    def upload(self,data)->tuple:
        try:
            _bike_instace=self.__createBike(data=data)
    
            _bikemeta_instace=self.__createBikeMeta(bike=_bike_instace,data=data['bike_meta'])

            _bike_instace.save()
            _bikemeta_instace.save()
           
       
            if data['bike_image']:
                threads=[]
                for i in data['bike_image']:
                    t=Thread(target=self.createBikeImages,args=(_bike_instace,i))
                    t.start()
                    threads.append(t)

                for thread in threads:
                    res=thread.join()
                    res.save()
                    
            return ({
                "message":"bike info is created!",
                "bike":BikeSerializer(instance=_bike_instace).data
            },status.HTTP_201_CREATED)
            
        except Exception as e:
            raise Exception(str(e))