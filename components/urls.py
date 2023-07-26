# -------------------------------------------------------------
# components/url.py
# 组分计算功能url声明
# -------------------------------------------------------------
from django.urls import path
from . import views


urlpatterns = [
    path('mass', views.mass_view),
    path('volume', views.volume_view),
    path('massup', views.mass_upload_view),
    path('volumeup', views.volume_upload_view)
    ]