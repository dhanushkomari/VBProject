from .models import VersionSetting, Voice
from rest_framework import serializers

class VersionSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionSetting
        fields = '__all__'

class VoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voice
        fields = '__all__'
