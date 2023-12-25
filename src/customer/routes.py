from django.urls import path
from src.customer.views.get_views import GetBikeViews

urlpatterns=[
    path('get-bikes&model_id=<str:model_id>&model_name=<str:model_name>/',GetBikeViews.as_view())
]