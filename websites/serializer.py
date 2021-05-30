from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, Project

class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo','contact',)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title','link']


class UserSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer(read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['username','profile','projects']







# class ProfileSerializer(serializers.ModelSerializer):
#     # user = UserSerializer(many=True, read_only=True)
#     class Meta:
#         model = Profile
#         fields = ('user','bio', 'contact',)