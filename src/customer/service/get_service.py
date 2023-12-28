from rest_framework import status
from src.customer.serializer.bike_serializer import BikeSerializer
from src.admins.models import Bike

class GetBikeService:

    def get(self,query:dict)->tuple:
        try:
            #if model_name=='none':
            #    if model_id=='all':
            #        bike=Bike.objects.all()
            #        data=BikeSerializer(bike,many=True).data
#
            #    else:
            #        if not Bike.objects.filter(bike_model_id=model_id).exists():
            #            raise Exception("wrong model id!")
            #        bike=Bike.objects.get(bike_model_id=model_id)
            #        data=BikeSerializer(instance=bike).data
#
            #elif model_name and model_id=='none':
            #    if not Bike.objects.filter(bike_model=model_name).exists():
            #            raise Exception("wrong model name!")
            #    
            #    bike=Bike.objects.filter(bike_model=model_name)
            #    data=BikeSerializer(instance=bike,many=True).data
            #
            #else:
                #raise Exception("you pass params in wrong way!")

            #if model_id:
            #    if not Bike.objects.filter(bike_model_id=model_id).exists():
            #            raise Exception("wrong model id!")
            #    bike=Bike.objects.get(bike_model_id=model_id)
            #    data=BikeSerializer(instance=bike).data
#
            #elif model_name:
            #    if not Bike.objects.filter(bike_model=model_name).exists():
            #            raise Exception("wrong model name!")
            #    
            #    bike=Bike.objects.filter(bike_model=model_name)
            #    data=BikeSerializer(instance=bike,many=True).data
            #
            #else:
            #    bike=Bike.objects.all()
            #    data=BikeSerializer(bike,many=True).data

            if not query:
                bike=Bike.objects.all()
                data=BikeSerializer(bike,many=True).data
            
            elif query.get('model_id') and len(query)==1:
                if not Bike.objects.filter(bike_model_id=query.get('model_id')).exists():
                        raise Exception("wrong model id!")
                bike=Bike.objects.get(bike_model_id=query.get('model_id'))
                data=BikeSerializer(instance=bike).data
            
            elif query.get('model_name') and len(query)==1:
                if not Bike.objects.filter(bike_model=query.get('model_name')).exists():
                        raise Exception("wrong model name!")
                
                bike=Bike.objects.filter(bike_model=query.get('model_name'))
                data=BikeSerializer(instance=bike,many=True).data 
            
            else:
                raise Exception("you pass params in wrong way. You must pass either /get-bikes/ or /get-bikes?model_id=<model_id>/ or /get-bikes?model_name=<model_name>/")

            return (
                    {"bikes":data},
                    status.HTTP_200_OK
                )
        except Exception as e:
            raise Exception(str(e))