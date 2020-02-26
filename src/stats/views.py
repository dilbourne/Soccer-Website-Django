from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
def stats_home(request):
    return render(request,"stats/stats_home.html")


def polar_scatter(request):
    return render(request,"stats/polar_scatter.html")
