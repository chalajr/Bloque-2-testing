from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

# Register your models here.

admin.site.site_header = "Educap Admin Panel"
admin.site.site_title = "Educap Admin Panel"
admin.site.index_title = "Bienvenido al panel administrativo de Educap"


class UserAdmin(BaseUserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'groups')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )
    ordering = ('email',)
    list_display = ('email', 'first_name', 'is_staff', 'last_login')
    list_filter = ('is_active', 'is_staff', 'groups')
    search_fields = ('email',)


# class LessonAdmin(admin.ModelAdmin):
#     fields = [.....]  # here comes the fields open to all users

#     # override default admin change behaviour
#     def change_view(self, request, object_id, extra_context=None):
#         if request.user in gruop2:  # an example
#             self.fields.append('field2')  # add field 2 to your `fields`
#             self.fields.append('field3')  # add field 3 to your `fields`


admin.site.register(UserModel, UserAdmin)
