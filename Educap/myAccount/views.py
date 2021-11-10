from django.db.models.deletion import ProtectedError
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from accounts.models import *
from .forms import *
import logging
from django.contrib.auth.decorators import login_required
# Create your views here.


def studentCreate(request):
    # Metodo post para el registro
    if request.method == "POST":

        # Guardamos formularios con el contenido enviado por el usuario en las variables
        studentFormRequest = StudentForm(request.POST, prefix='student')
        userFormRequest = UserForm(request.POST, prefix='user')

        # Revisamos que los formularios del usuario sea correcto
        if studentFormRequest.is_valid() and userFormRequest.is_valid():

            logging.error("Es valido")

            # Guardado y creacion del nuevo usuario
            # Se guarda el registro de usuario
            userFormRequest.save()
            userFormSave = userFormRequest.save()

            # Se crea el registro del estudiante pero no se guarda
            studentFormSave = studentFormRequest.save(commit=False)
            # Asignamos el usuario al estudiante
            studentFormSave.user = userFormSave
            # Guardamos el estudiante
            studentFormSave.save()
            return render(request, "myAccount/successfulStudentCreate.html")
        else:
            logging.error("Es invalido")
            return render(request, "myAccount/studentCreate.html", {
                "studentForm": studentFormRequest,
                "userForm": userFormRequest
            })
    return render(request, "myAccount/studentCreate.html", {
        "studentForm": StudentForm(prefix='student'),
        "userForm": UserForm(prefix='user')
    })


@login_required(login_url="login")
def studentRead(request):
    if request.user.is_staff:
        return redirect('admin:index')
    # Obtenemos el objeto de usuario con request.user
    user = UserModel.objects.get(pk=request.user.pk)
    # Obtenemos el objeto de estudiante refiriendonos al usuario
    student = Estudiante.objects.get(user=user)

    return render(request, "myAccount/studentRead.html", {
        "user": user,
        "student": student
    })


@login_required(login_url="login")
def studentUpdate(request):
    # Obtenemos el objeto de usuario con request.user
    user = UserModel.objects.get(pk=request.user.pk)
    # Obtenemos el objeto de estudiante refiriendonos al usuario
    student = Estudiante.objects.get(user=user)
    # Metodo post para el registro
    if request.method == "POST":

        # Guardamos formularios con el contenido enviado por el usuario en las variables
        studentFormRequest = StudentForm(
            request.POST, prefix='student', instance=student)
        userFormRequest = userFormChange(
            request.POST, prefix='user', instance=user)

        # Revisamos que los formularios del usuario sea correcto
        if studentFormRequest.is_valid() and userFormRequest.is_valid():

            logging.error("Es valido")

            # Guardado y creacion del nuevo usuario
            # Se guarda el registro de usuario
            userFormRequest.save()
            userFormSave = userFormRequest.save()

            # Se crea el registro del estudiante pero no se guarda
            studentFormSave = studentFormRequest.save(commit=False)
            # Asignamos el usuario al estudiante
            studentFormSave.user = userFormSave
            # Guardamos el estudiante
            studentFormSave.save()
            return render(request, "myAccount/successfulStudentUpdate.html")
        else:
            logging.error("Es invalido")
            return render(request, "myAccount/studentModify.html", {
                "studentForm": studentFormRequest,
                "userForm": userFormRequest
            })
    return render(request, "myAccount/studentModify.html", {
        "studentForm": StudentForm(prefix='student', instance=student),
        "userForm": userFormChange(prefix='user', instance=user)
    })


@login_required(login_url="login")
def studentDelete(request):
    return


@login_required(login_url="login")
def myAccount(request):
    if request.user.is_staff:
        return redirect('admin:index')
    return render(request, "myAccount/myAccount.html", {

    })


@login_required(login_url="login")
def followedLessons(request):
    if request.user.is_staff:
        return redirect('admin:index')
    estudiante = Estudiante.objects.get(user=request.user)
    estudianteLecciones = Estudiante_Lecciones.objects.filter(
        estudiante=estudiante)
    return render(request, "myAccount/lessonsList.html", {
        "lessons": estudianteLecciones
    })


@login_required(login_url="login")
def loginRedirect(request):
    if request.user.is_staff:
        return redirect('admin:index')
    else:
        return redirect('LearningCatalog:listLesson')
