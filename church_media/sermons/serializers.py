from rest_framework import serializers
from .models import Sermon

""" turn objects into json format"""
class SermonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sermon
        fields = ['id', 'title', 'preacher', 'date', 'content', 'added_by', 'created_at', 'updated_at', 'category']
        read_only_fields = ['id', 'added_by', 'created_at', 'updated_at']
