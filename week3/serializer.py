from rest_framework import serializers
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['title', 'description', 'image', 'author', 'created_date', 'author_profile', 'link']