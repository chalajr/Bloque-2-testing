from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator

# Create your models here.

ROLES = [
    ('INT', 'Instructor'),
    ('ADM', 'Administrador'),
    ('CRV', 'Revisor de contenido')
]


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class UserModel(AbstractUser):
    username = None
    email = models.EmailField('Correo electronico', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    pass

    class meta:
        pass

    objects = UserManager()

    def __str__(self):
        return self.email


class MiembroStaff(models.Model):
    user = models.OneToOneField(UserModel, on_delete=CASCADE)
    role = models.CharField(choices=ROLES, max_length=5)


class Estudiante(models.Model):
    user = models.OneToOneField(UserModel, on_delete=CASCADE)
    edad = models.PositiveSmallIntegerField()
