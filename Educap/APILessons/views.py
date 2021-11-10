from django.http.response import HttpResponse
from django.shortcuts import render
from . import urls
from LearningCatalog.models import Categoria
import logging
# Create your views here.


def test(request):
    token = request.GET.get('token')
    logging.error(token)
    return HttpResponse('BXAKLSJHDAS(*&(*&978918273')
