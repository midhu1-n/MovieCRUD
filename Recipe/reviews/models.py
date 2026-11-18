from django.db import models

from recipes.models import Recipe
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    rating=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    #
    # def __str__(self): #string representation of object
    #     # return self.user.username
    #     return self.recipe_name
