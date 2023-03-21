# -------------------------------------------------------------
# components/url.py
# 组分计算功能url声明
# -------------------------------------------------------------
from django.urls import path
from . import views


urlpatterns = [
    path('mass', views.mass_view),
    path('volume', views.volume_view)
    ]