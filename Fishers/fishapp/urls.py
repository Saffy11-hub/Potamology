from django.urls import path
from . import views


urlpatterns = [
    path('', views.Slack, name="Home"),
]
