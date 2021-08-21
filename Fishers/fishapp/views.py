from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def Slack(request):
    return HttpResponse('<h1>Safi Monday</h1>')
