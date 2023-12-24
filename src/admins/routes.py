from django.urls import path
from src.admins.views.upload_bike_views import UploadBikeViews
from src.admins.views.get_bike_views import GetBikeViews

urlpatterns=[
    path('upload/',UploadBikeViews.as_view()),
    path('get-bikes&model_id=<str:model_id>/',GetBikeViews.as_view())
]