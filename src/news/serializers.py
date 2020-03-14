from rest_framework import serializers
from .models import UserProfile, Headline

class DailyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        fields = '__all__'