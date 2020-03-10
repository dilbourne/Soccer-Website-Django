from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import PlayerInfoSerializer, ForwardStatsSerializer, MidfielderStatsSerializer, DefenderStatsSerializer, GoalkeeperStatsSerializer 
from .models import PlayerInfo, ForwardStats, MidfielderStats, DefenderStats, GoalkeeperStats
from django.http import HttpResponse
# Create your views here.
class PlayerInfoViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerInfoSerializer
    queryset = PlayerInfo.objects.all()
    lookup_field = 'name'
    
    '''def get_queryset(self):
        name = self.kwargs.get('pk',None)
        if name is not None:
            return PlayerInfo.objects.filter(name=name)
            
        else:
            return PlayerInfo.objects.all()'''
    
        
    

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

