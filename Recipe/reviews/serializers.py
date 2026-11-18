from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from accounts.serializers import UserSerializer
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from reviews.models import Review
class ReviewSerializer(serializers.ModelSerializer):

    #nested Serializer
    # user=UserSerializer(read_only=True)
    # recipe=RecipeSerializer(read_only=True)

    user=StringRelatedField()
    recipe=StringRelatedField()
    #Displays the related objects using its string representation defined by inside
    #__str__
    #
    # message=serializers.SerializerMethodField()
    # user= serializers.SerializerMethodField()
    # recipe= serializers.SerializerMethodField()
    # msg2=serializers.SerializerMethodField()
    class Meta:
        model=Review
        fields='__all__'
        read_only_fields=['user','created_at']

    # def get_message(self,obj):
    #     return "hello"
    #
    # def get_user(self,obj):
    #     return obj.user.email
    # def get_recipe(self,obj):
    #     return obj.recipe.recipe_name
    #
    # def get_msg2(self,obj):
    #     return "thank you"



