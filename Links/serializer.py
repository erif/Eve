#Serializer class for Links
from django.forms import widgets
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    """docstring for LinkSerializer"""
    class Meta:
        model = Link
        fields = ('id', 'name', 'description', 'linkURL', 'date_posted', 'posted_by')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

