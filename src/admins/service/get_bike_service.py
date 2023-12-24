from rest_framework import status
from src.admins.serializer.bike_serializer import BikeSerializer
from src.admins.models import Bike

class GetBikeService:

    def get(self,model_id)->tuple:
        try:
            if model_id=='all':
                bike=Bike.objects.all()
                data=BikeSerializer(bike,many=True).data

            else:
                if not Bike.objects.filter(bike_model_id=model_id).exists():
                    raise Exception("wrong model id!")
                bike=Bike.objects.get(bike_model_id=model_id)
                data=BikeSerializer(instance=bike).data

            return (
                    {"bikes":data},
                    status.HTTP_200_OK
                )
        except Exception as e:
            raise Exception(str(e))