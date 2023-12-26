from django.urls import path
from src.admins.views.upload_views import UploadBikeViews
from src.admins.views.modify_views import ModifyViews
from src.admins.views.uploadimages_views import UploadImagesViews
from src.admins.views.delete_views import DeleteViews

urlpatterns=[
    path('upload/',UploadBikeViews.as_view()),
    path('modify/',ModifyViews.as_view()),
    path('upload/images/model_id=<str:model_id>/',UploadImagesViews.as_view()),
    path('delete/',DeleteViews.as_view()),
]