from django.urls import path
from src.admins.views.upload_views import UploadBikeViews

urlpatterns=[
    path('upload/',UploadBikeViews.as_view()),
]