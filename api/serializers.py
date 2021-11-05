from .models import VersionSetting, Voice, FlatVersionSettings
from rest_framework import serializers

class VersionSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionSetting
        fields = '__all__'

class VoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voice
        fields = '__all__'

class FlatVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlatVersionSettings
        fields = '__all__'
