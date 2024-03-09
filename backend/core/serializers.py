from rest_framework import serializers
from core.models import SmallingoVideo

class SmallingoVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmallingoVideo
        fields = ['url', 'video_thumbnail']

class SmallingoVideoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmallingoVideo
        fields = ['url']
