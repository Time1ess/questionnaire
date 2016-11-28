from django.contrib import admin

from school.models import *

# Register your models here.

RegisterClass = (
    SchoolAdmin,
)

for item in RegisterClass:
    admin.site.register(item)
