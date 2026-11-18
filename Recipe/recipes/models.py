from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name=models.CharField(max_length=30)
    ingredients=models.CharField(max_length=30)
    instructions=models.TextField()
    options=(('breakfast','Breakfast'),('lunch','Lunch'),('dinner','Dinner'))
    mealtype=models.CharField(max_length=30,choices=options)
    types=(('indian','Indian'),('italian','Italian'),('chinese','Chinese'))
    cuisine=models.CharField(max_length=30,choices=types)
    image=models.ImageField(null=True,upload_to="recipes")

    def __str__(self):
      return self.recipe_name