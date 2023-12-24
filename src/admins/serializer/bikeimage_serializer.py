from rest_framework import serializers
from src.admins.models import BikeImages

class BikeImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model=BikeImages
        fields=(
            'bikeimage_id',
            'image_name',
            'image_path'
        )