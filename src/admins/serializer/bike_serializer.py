from rest_framework import serializers
from rest_framework.fields import empty
from src.admins.models import Bike
from src.admins.serializer.bikemeta_serializer import BikeMetaSerializer
from src.admins.serializer.bikeimage_serializer import BikeImagesSerializer

class BikeSerializer(serializers.ModelSerializer):

    bike_meta=BikeMetaSerializer(many=True)
    bike_image=BikeImagesSerializer(many=True)
    
    class Meta:
        model=Bike
        fields=('bike_model_id','bike_model','brand_name','bike_name','image_path','image_name','bike_meta','bike_image')

