from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from . import views

app_name = "myAccount"

urlpatterns = [
    path('', views.myAccount, name="myAccount"),
    path('Registro/', views.studentCreate, name="studentCreate"),
    path('Modificar/', views.studentUpdate, name="studentUpdate"),
    path('Información/', views.studentRead, name="studentRead"),
    path('Baja', views.studentDelete, name="studentDelete"),
    path('LeccionesQueSigo/', views.followedLessons, name="followedLessons"),
    path('Redirect/', views.loginRedirect, name="loginRedirect")
]
