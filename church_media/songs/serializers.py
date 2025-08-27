from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'lyrics', 'category', 'created_at', 'updated_at', 'artist', 'added_by']
        read_only_fields = ['id','added_by', 'created_at', 'updated_at']