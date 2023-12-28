from django.urls import path,re_path
from src.customer.views.get_views import GetBikeViews

"""
For get bikes: 
url1 = 'get-bikes?model_id=abc/'
url2 = 'get-bikes?model_name=abc/'
url3 = 'get-bikes/'
"""

urlpatterns=[
    re_path(r'^get-bikes(?:\?model_id=[a-zA-Z0-9_-]+)?(?:\?model_name=[a-zA-Z0-9_-]+)?/$', GetBikeViews.as_view()),
]