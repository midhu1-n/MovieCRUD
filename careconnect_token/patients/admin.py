from django.contrib import admin

# Register your models here.
from patients.models import Appointment
admin.site.register(Appointment)
