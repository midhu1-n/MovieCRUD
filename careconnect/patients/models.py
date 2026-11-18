from django.db import models
from doctors.models import Doctor
# Create your models here.

class Appointment(models.Model):
    patient_name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender_choices=(('female','Female'),('male','Male'))
    gender=models.CharField(max_length=20,choices=gender_choices)
    problem=models.TextField()
    phone=models.CharField(max_length=20)
    appointment_date=models.DateField()
    appointment_time=models.TimeField(null=True)
    token_number=models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True) #date in which record is saved in db table
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)

