from django.contrib import admin

# Register your models here.
from app.models import Movie,CustomUser
admin.site.register(Movie)
admin.site.register(CustomUser)