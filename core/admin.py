from django.contrib import admin
from .models import TypePerson,Person,Movie,Comments,Genre

admin.site.register([TypePerson,Person,Movie,Comments,Genre])
