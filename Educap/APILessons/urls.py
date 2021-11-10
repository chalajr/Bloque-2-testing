from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from . import views

app_name = "APILessons"

urlpatterns = [
    path('apiTesting', views.test, name='test'),
]
