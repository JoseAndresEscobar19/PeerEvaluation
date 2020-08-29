from django.contrib import admin

# Register your models here.
from .models import Group,Student

admin.site.register(Group)
admin.site.register(Student)