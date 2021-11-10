from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "LearningCatalog"

urlpatterns = [
    path('Categorias', views.primaryCategory, name='primaryCategory'),
    path('Categorias/<int:pk>', views.subCategories, name='subCategories'),
    path('Busqueda/Categorias', views.searchCategory, name="searchCategory"),
    path('Lecciones', views.listLesson, name="listLesson"),
    path('Lecciones/<int:pk>', views.readLesson, name="readLesson"),
    path('Busqueda/Lecciones', views.searchLesson, name="searchLesson"),
    path('Categoria/Lecciones/<int:pk>', views.filterLessonsByCategory,
         name="filterLessonsByCategory"),
    path('Lecciones/FollowLesson',
         views.followLesson, name="followLesson"),
    path('CheckFollow/', views.checkFollow, name="checkFollow")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
