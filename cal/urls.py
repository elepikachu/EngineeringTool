from django.urls import path
from . import views


urlpatterns = [
    path('steam', views.steam_view),
    ]