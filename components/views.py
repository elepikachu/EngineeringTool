# -------------------------------------------------------------
# components/views.py
# 组分计算功能视图函数
# -------------------------------------------------------------

from django.shortcuts import render

VERSION = 'Engineering Toolbox 1.0.0'


# -------------------------------------------------------------
# 函数名： mass_view
# 功能： 质量分数计算
# -------------------------------------------------------------
def mass_view(request):
    dic = {'ver': VERSION}
    return render(request, 'components/mass.html', dic)


# -------------------------------------------------------------
# 函数名： volume_view
# 功能： 体积分数计算
# -------------------------------------------------------------
def volume_view(request):
    dic = {'ver': VERSION}
    return render(request, 'components/volume.html', dic)

