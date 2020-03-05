from rest_framework import serializers
from .models import PlayerInfo, ForwardStats, MidfielderStats, DefenderStats, GoalkeeperStats

class PlayerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerInfo
        fields = '__all__'

class ForwardStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForwardStats
        fields = '__all__'

class MidfielderStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MidfielderStats
        fields = '__all__'

class DefenderStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefenderStats
        fields = '__all__'

class GoalkeeperStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalkeeperStats
        fields = '__all__'
