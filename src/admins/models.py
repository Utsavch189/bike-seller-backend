from django.db import models
from datetime import datetime

class Bike(models.Model):
    bike_model_id=models.CharField(max_length=100,primary_key=True,default="")
    bike_model=models.CharField(max_length=100,null=True,blank=True)
    brand_name=models.CharField(max_length=100,null=True,blank=True)
    bike_name=models.TextField(null=True,blank=True,default="")
    image_path=models.TextField(null=True,blank=True,default="")
    image_name=models.CharField(max_length=100,null=True,blank=True,unique=True)

    def __str__(self) -> str:
        return self.bike_model

class BikeMeta(models.Model):
    bikemeta_id=models.CharField(max_length=100,primary_key=True,default="")
    bike=models.ForeignKey(Bike,on_delete=models.CASCADE,related_name='bike_meta')
    asking_price=models.CharField(max_length=10,null=True,blank=True)
    year_of_model=models.CharField(max_length=10,null=True,blank=True)
    engine_cc=models.CharField(max_length=10,null=True,blank=True)
    engine_type=models.CharField(max_length=50,null=True,blank=True)
    kms_run=models.CharField(max_length=50,null=True,blank=True)
    no_of_owners=models.CharField(max_length=50,null=True,blank=True)
    available=models.CharField(max_length=50,null=True,blank=True)
    mileage=models.CharField(max_length=50,null=True,blank=True)
    buy_year=models.CharField(max_length=10,null=True,blank=True)
    color=models.CharField(max_length=50,null=True,blank=True)
    details=models.TextField(null=True,blank=True,default="")
    latest_upload=models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.bike.bike_model

class BikeImages(models.Model):
    bikeimage_id=models.CharField(max_length=100,primary_key=True,default="")
    bike=models.ForeignKey(Bike,on_delete=models.CASCADE,related_name='bike_image')
    image_path=models.TextField(null=True,blank=True,default="")
    image_name=models.TextField(null=True,blank=True,default="")

    def __str__(self) -> str:
        return self.bike.bike_model
