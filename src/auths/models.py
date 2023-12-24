from django.contrib.auth.models import AbstractUser
from django.db import models

USER_TYPES=(
    ('admin','admin'),
    ('customer','customer')
)

class Client(AbstractUser):
    phone=models.CharField(max_length=10,null=True,blank=True)
    user_type=models.CharField(max_length=15,choices=USER_TYPES,default='customer')

    class Meta:
        __name__='Client'

    def __str__(self) -> str:
        return self.username

from django.contrib.auth.base_user import BaseUserManager

class Clientmanager(BaseUserManager):
    def create_user(self,password=None,**extra):
        user=self.model(**extra)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,password=None,**extra):
        extra.setdefault('is_staff',True)
        extra.setdefault('is_superuser',True)
        extra.setdefault('is_active',True)
        return self.create_user(password,**extra)