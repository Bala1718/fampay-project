from rest_framework import serializers
from api_code.models import Youtubevideo


class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtubevideo
        fields = '__all__'
        # exclude = ('id')