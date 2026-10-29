from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    empid=models.IntegerField(unique=True)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    gender_choices=(('male','Male'),('female','Female'))
    gender=models.CharField(max_length=30,choices=gender_choices)
    joining_date=models.DateField(auto_now_add=True)
    salary=models.IntegerField()
    designation=models.CharField(max_length=30)
    image=models.ImageField(null=True,upload_to="employees")


    #auto_now_add=True  --automatically adds current date to employee record
    #from client side we dont have to send joining_date it will create automatically

