from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .serializers import PlayerInfoSerializer, ForwardStatsSerializer, MidfielderStatsSerializer, DefenderStatsSerializer, GoalkeeperStatsSerializer, NationalityCountSerializer 
from .models import PlayerInfo, ForwardStats, MidfielderStats, DefenderStats, GoalkeeperStats
from django.http import HttpResponse
from django.db.models import Count
from .getters import getHeadingsAndAbbreviations, getTableBodyData


# Create your views here.
class PlayerInfoViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerInfoSerializer
    queryset = PlayerInfo.objects.all()
    lookup_field = 'name'
    
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

class NationalityCountViewSet(APIView):
    def get(self, request, n=None):
        qs_length = len(PlayerInfo.objects.values('country').annotate(Count('country',distinct=False)))
        if n == None or n > qs_length:
            queryset = PlayerInfo.objects.values('country').annotate(Count('country',distinct=False)).order_by('-country__count')
            return Response(NationalityCountSerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        elif n > 0:
            queryset = PlayerInfo.objects.values('country').annotate(Count('country',distinct=False)).order_by('-country__count')[0:n]
            print(NationalityCountSerializer(queryset,many=True).data)
            return Response(NationalityCountSerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        else:
            return Response({"error": "parameter must be a positive integer."}, status=status.HTTP_404_NOT_FOUND)

class TableStandingsViewSet(APIView):
    def get(self, request):
        return Response(data=getTableBodyData(getHeadingsAndAbbreviations()), status=status.HTTP_200_OK)


def stats_home(request):
    return render(request,"stats/stats_home.html")


def polar_scatter(request):
    return render(request,"stats/polar_scatter.html")

