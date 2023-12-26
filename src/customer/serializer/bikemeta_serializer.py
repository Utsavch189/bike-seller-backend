from rest_framework import serializers
from src.admins.models import BikeMeta

class BikeMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model=BikeMeta
        fields=(
            'bikemeta_id',
            'bike',
            'asking_price',
            'year_of_model',
            'engine_cc',
            'engine_type',
            'kms_run',
            'no_of_owners',
            'available',
            'mileage',
            'buy_year',
            'color',
            'details',
            'latest_upload'
        )