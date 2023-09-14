from rest_framework import serializers
from .models import Scrapa

class ScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrapa
        fields = ('id', 'channel_id', 'channel_title', 'title', 'video_id', 'published_at', 'transcript', 'sentiment')