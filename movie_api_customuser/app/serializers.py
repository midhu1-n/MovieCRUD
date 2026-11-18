from rest_framework import serializers
from app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
from django.contrib.auth.models import User
from django.core.mail import send_mail
from app.models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','password','email',
                'first_name','last_name'
                ,'phone','address']

    def create(self,validated_data):
         u=CustomUser.objects.create_user(**validated_data)
         # to encrypt the password/password hashing we redefine create()
         # in our UserSerializer class

         # For creating a user account
         # User.objects.create_user(**validated_data),automatically it will encrypt the password

         # For creating a superuser
         # User.objects.create_superuser(**validated_data),automatically it will create
         # user as admin
         u.save()

         send_mail(
             subject="welcome to our app",
             message="Thank you for signing up for an account",
             from_email="midhunmp493@gmail.com",
             recipient_list=[u.email],
             fail_silently=False)


         return u


