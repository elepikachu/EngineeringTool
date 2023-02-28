from django.shortcuts import render

VERSION = 'Engineering Toolbox 1.0.0'


# -------------------------------------------------------------
# 函数名： main_view
# 功能： 网站首页
# -------------------------------------------------------------
def main_view(request):
    dic = {'ver': VERSION}
    return render(request, 'main.html', dic)


def cxk_view(request):
    dic = {'ver': VERSION}
    return render(request, 'kun.html', dic)


def choose_view(request):
    dic = {'ver': VERSION}
    return render(request, 'choose.html', dic)