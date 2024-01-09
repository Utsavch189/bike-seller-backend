from rest_framework import status
from src.customer.serializer.bike_serializer import BikeSerializer
from src.admins.models import Bike
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


class GetBikeService:

    def get(self,query:dict)->tuple:
        try:
            count=bike=Bike.objects.count()
            if not query:
                bike=Bike.objects.all()
                data=BikeSerializer(bike,many=True).data
            
            elif query.get('page') and query.get('page-size') and len(query)==2:
                bike=Bike.objects.all().order_by('bike_model_id')
                paginator=Paginator(bike,query.get('page-size'))
                try:
                    query=paginator.page(query.get('page'))
                except PageNotAnInteger:
                    query=paginator.page(1)
                except EmptyPage:
                    query=paginator.page(paginator.num_pages)
                data=BikeSerializer(query,many=True).data
            
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
                    {"bikes":data,"total_bikes":count},
                    status.HTTP_200_OK
                )
        except Exception as e:
            raise Exception(str(e))
    
