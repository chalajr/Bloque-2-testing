from django.http.response import HttpResponse
from django.shortcuts import render
from . import urls
from LearningCatalog.models import Categoria
import logging
from .models import *
from accounts.models import *
import json
from copy import copy
# Create your views here.


def primaryCategory(request):
    # Respuesta HTTPS donde django procesa el html y presenta la ingerfaz
    return render(request, "LearningCatalog/primaryCategory.html", {
        # Contexto para procesar la interfaz donde se realiza un query a la base de datos y obtenemos todas las categorias
        "categories": Categoria.objects.all(),

    })


def subCategories(request, pk):
    category = Categoria.objects.get(pk=pk)
    subCategory = Categoria.objects.filter(categoriaPadre=category)
    logging.error(subCategory)
    return render(request, "LearningCatalog/subcategory.html", {
        "category": Categoria.objects.get(pk=pk),
        "subCategories": subCategory,
    })


def searchCategory(request):
    if request.method == "POST":
        search = request.POST.get('searchBar')
        return render(request, "LearningCatalog/searchBar.html", {
            "categories": Categoria.objects.filter(nombre__icontains=search),
        })


def listLesson(request):
    lessons = Leccion.objects.all()
    return render(request, "LearningCatalog/lessonList.html", {
        "lessons": lessons
    })


def readLesson(request, pk):
    lesson = Leccion.objects.get(pk=pk)
    files = Archivo.objects.filter(leccion=pk).order_by('orden')
    videos = Video.objects.filter(leccion=pk)
    
    # Convertir urls de youtube a urls de Embed


    arrVidL=[video.link for video in videos] 
    arrVidT=[video.titulo for video in videos] 
    arrVidD=[video.descripcion for video in videos] 
    
    videoCode=[]
    vidLists= []
    for i in arrVidL:
        arrLinks = []
        arrLinks = i.split('/')
        
        videoCode.append(arrLinks[3])
    

    vidLists=list(zip(arrVidT, arrVidD, videoCode))
    
    
    ##############################################

    leccion = Leccion.objects.get(pk=pk)

    if request.user.is_anonymous:
        follow = True
    else:
        if request.user.is_staff:

            follow = False
        else:
            estudiante = Estudiante.objects.get(user=request.user)
            if Estudiante_Lecciones.objects.filter(estudiante=estudiante, leccion=leccion).exists():
                follow = True
            else:
                follow = False
    return render(request, "LearningCatalog/lesson.html", {
        "lesson": lesson,
        "files": files,
        "follow": follow,
        "vidLists": vidLists,
        
  
    })


def searchLesson(request):
    if request.method == "POST":
        search = request.POST.get('searchBar')
        return render(request, "LearningCatalog/lessonList.html", {
            "lessons": Leccion.objects.filter(titulo__icontains=search),
        })


def filterLessonsByCategory(request, pk):
    subCategory = Categoria.objects.get(pk=pk)
    lessons = Leccion.objects.filter(category=subCategory)
    return render(request, "LearningCatalog/lessonList.html", {
        "lessons": lessons
    })


def followLesson(request):
    if request.is_ajax():
        if request.method == "POST":
            jsonObject = json.load(request)['jsonBody']
            pk = jsonObject["pk"]
            estudiante = Estudiante.objects.get(user=request.user)
            leccion = Leccion.objects.get(pk=pk)
            if Estudiante_Lecciones.objects.filter(estudiante=estudiante, leccion=leccion).exists():
                newUnfollow = Estudiante_Lecciones.objects.get(
                    estudiante=estudiante,
                    leccion=leccion
                )
                newUnfollow.delete()
                return HttpResponse("follow")
            else:
                newFollow = Estudiante_Lecciones(
                    estudiante=estudiante,
                    leccion=leccion
                )
                newFollow.save()
                return HttpResponse("unFollow")


def checkFollow(request):
    return HttpResponse()
