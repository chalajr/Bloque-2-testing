from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

app_name = "APIAccounts"

urlpatterns = [
    path('auth/register/user', RegisterView.as_view()),
    path('auth/login', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('auth/refresh', TokenRefreshView.as_view(), name="token_refresh"),
]
