from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import UserModel, Estudiante
# Creacion de modelos.

# Tipos de archivos para determinar cual icono utilizaremos en la interfaz
FILETYPES = [
    ('PDF', 'Archivo PDF'),
    ('IMG', 'Imagen'),
    ('DOC', 'Archivo Word'),
    ('PPX', 'PowerPoint'),
    ('XLX', 'Archivo Excel'),
    ('ANY', 'Archivo')
]

# Clase de modelos para crear las tablas en la base de datos


class Categoria(models.Model):
    # Todos los atributos vienen de la importacion de models y son clases predefinidas de django para la creacion de tablas
    nombre = models.CharField("Nombre", max_length=30)
    descripcion = models.TextField("Descripción", max_length=100)
    imagen = models.ImageField("Imagen", upload_to='uploads/categories/img')
    fechaCreada = models.DateTimeField("Fecha de creación", auto_now_add=True)
    # Atributo que se refiere a la misma clase para poder tener nesting de categorias
    categoriaPadre = models.ForeignKey(
        'self', blank=True, null=True, on_delete=CASCADE, verbose_name="Categoria perteneciente")

    def __str__(self):
        return f"{self.pk} {self.nombre}"


class Leccion(models.Model):

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField("Descripción", max_length=500)
    imagen = models.ImageField(upload_to='uploads/lessons/img')
    fecha = models.DateField(
        "Fecha de creación", auto_now=False, auto_now_add=True)
    aprobacion = models.BooleanField("Aprobación", default=False)
    category = models.ForeignKey(
        Categoria, on_delete=CASCADE, verbose_name="Categoria")
    # Verbose name y verbose name plural para cambiar el nombre de la seccion en el panel administrativo
    created_by = models.ForeignKey(UserModel, on_delete=CASCADE)

    class Meta:
        verbose_name = ("Lección")
        verbose_name_plural = ("Lecciones")


class Archivo(models.Model):
    orden = models.SmallIntegerField("Orden de aparición")
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField("Descripción", max_length=500)
    path = models.FileField("Archivo", upload_to='uploads/files')
    lipo = models.CharField("Tipo de archivo", choices=FILETYPES, max_length=3)
    leccion = models.ForeignKey(Leccion, on_delete=CASCADE)


class Video(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField("Descripción", max_length=500)
    link = models.CharField(max_length=500)
    leccion = models.ForeignKey(Leccion, on_delete=CASCADE)


class Estudiante_Lecciones(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=CASCADE)
    leccion = models.ForeignKey(Leccion, on_delete=CASCADE)
