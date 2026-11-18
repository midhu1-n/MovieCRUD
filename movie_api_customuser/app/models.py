from django.db import models

# Create your models here.

class Movie(models.Model):
    title=models.CharField(max_length=30)
    director=models.CharField(max_length=30)
    language=models.CharField(max_length=30)
    # year=models.IntegerField()
    rating=models.FloatField()
    runtime=models.IntegerField()
    image=models.ImageField(upload_to="movies",null=True,blank=True)
#CustomUser definition
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    #username,password,email,first_name,last_name
    #this model already extends the existing models so only new fields are added
    phone=models.CharField(max_length=50,null=True)
    address=models.TextField(null=True)

