from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from users.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name','home_club','strong_hand','city','achievements','date_of_birth','profession','role_model')






# class UserSerializer(serializers.ModelSerializer): #USER LOGIN/LOGOUT REGISTRATION
#  
#     email = serializers.EmailField(
#         required=True,
#         validators = [UniqueValidator(queryset=User.objects.all())]
#         )
#     username = serializers.CharField(
#             max_length=20,
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )
#     # first_name = serializers.CharField(
#     #     required=True,
#     #     max_length=50
#     #     ) 
#     # last_name =  serializers.CharField(
#     #     required=True,
#     #     max_length=50
#     #     )
#     password = serializers.CharField(min_length=8,write_only=True)

#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'],
#              validated_data['password'])
#         # user.last_name = last_name
#         # user.first_name = first_name
#         # user.save()
#         return user

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')


        