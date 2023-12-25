from rest_framework import status
from src.customer.serializer.bike_serializer import BikeSerializer
from src.admins.models import Bike

class GetBikeService:

    def get(self,model_id:str,model_name:str)->tuple:
        try:
            if model_name=='none':
                if model_id=='all':
                    bike=Bike.objects.all()
                    data=BikeSerializer(bike,many=True).data

                else:
                    if not Bike.objects.filter(bike_model_id=model_id).exists():
                        raise Exception("wrong model id!")
                    bike=Bike.objects.get(bike_model_id=model_id)
                    data=BikeSerializer(instance=bike).data

            elif model_name and model_id=='none':
                if not Bike.objects.filter(bike_model=model_name).exists():
                        raise Exception("wrong model name!")
                
                bike=Bike.objects.filter(bike_model=model_name)
                data=BikeSerializer(instance=bike,many=True).data
            
            else:
                raise Exception("you pass params in wrong way!")

            return (
                    {"bikes":data},
                    status.HTTP_200_OK
                )
        except Exception as e:
            raise Exception(str(e))