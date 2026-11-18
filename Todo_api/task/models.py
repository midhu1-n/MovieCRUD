from django.db import models
# Create your models here.
from django.contrib.auth.models import User
class task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=30)
    created=models.DateTimeField(auto_now_add=True) #date in which record is saved in db table
    completed=models.BooleanField()
