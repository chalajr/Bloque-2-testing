from django.contrib import admin
from .models import *
import string
import logging
# Register your models here.


class AlphabetFilter(admin.SimpleListFilter):
    title = 'alfabeto'
    parameter_name = 'alfabeto'

    def lookups(self, request, model_admin):
        abc = list(string.ascii_lowercase)
        return ((c.upper(), c.upper()) for c in abc)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(nombre__startswith=self.value())


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pk', 'descripcion',
                    'fechaCreada', 'getCategoria')
    list_filter = ('fechaCreada',)
    search_fields = ['nombre', 'fechaCreada']
    ordering = ('nombre',)

    @admin.display(description='categoriaPadre')
    def getCategoria(self, obj):
        return obj.categoriaPadre


class ArchivoAdminInline(admin.TabularInline):
    model = Archivo


class VideoAdminInline(admin.TabularInline):
    model = (Video)


class LeccionAdmin(admin.ModelAdmin):
    inlines = (ArchivoAdminInline, VideoAdminInline)
    list_display = ('titulo', 'descripcion', 'fecha', 'aprobacion')
    search_fields = ['titulo', ]
    list_filter = ('fecha', 'aprobacion')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Leccion, LeccionAdmin)
