import shutil
from src.admins.models import Bike
from rest_framework import status

class DeleteBikeService:

    @staticmethod
    def delete(bike_model_id:str)->tuple:
        try:
            if not bike_model_id:
                raise Exception('model_id required!')
            
            if not Bike.objects.filter(bike_model_id=bike_model_id).exists():
                raise Exception("bike doesn't exists")
            
            bike=Bike.objects.get(bike_model_id=bike_model_id)
            shutil.rmtree(f'media/{bike.bike_model_id}')
            bike.delete()

            return (
                {"message":"deleted!"},
                status.HTTP_202_ACCEPTED
            )
        except Exception as e:
            raise Exception(str(e))