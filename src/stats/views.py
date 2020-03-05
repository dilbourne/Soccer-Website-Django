from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from rest_framework import viewsets
from .serializers import PlayerInfoSerializer, ForwardStatsSerializer, MidfielderStatsSerializer, DefenderStatsSerializer, GoalkeeperStatsSerializer 
from .models import PlayerInfo, ForwardStats, MidfielderStats, DefenderStats, GoalkeeperStats

# Create your views here.
class PlayerInfoViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerInfoSerializer
    def get_queryset(self):
        queryset = PlayerInfo.objects.all()
        name = self.request.query_params.get('name',None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset
    


class ForwardStatsViewSet(viewsets.ModelViewSet):
    queryset = ForwardStats.objects.all()
    serializer_class = ForwardStatsSerializer

class MidfielderStatsViewSet(viewsets.ModelViewSet):
    queryset = MidfielderStats.objects.all()
    serializer_class = MidfielderStatsSerializer

class DefenderStatsViewSet(viewsets.ModelViewSet):
    queryset = DefenderStats.objects.all()
    serializer_class = DefenderStatsSerializer

class GoalkeeperStatsViewSet(viewsets.ModelViewSet):
    queryset = GoalkeeperStats.objects.all()
    serializer_class = GoalkeeperStatsSerializer

def stats_home(request):
    return render(request,"stats/stats_home.html")


def polar_scatter(request):
    return render(request,"stats/polar_scatter.html")

