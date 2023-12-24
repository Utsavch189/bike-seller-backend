from django.urls import path
from src.auths.views.login_views import LoginView

urlpatterns = [
    path('login/',LoginView.as_view()),
]