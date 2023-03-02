from django.shortcuts import render
from .water_heatt_calculation import WaterHeatCalculation

VERSION = 'Engineering Toolbox 1.0.0'
DIC_PRS = {'Pa': 1, 'kPa': 1000, 'MPa': 1000000, 'atm': 101325}
DIC_TMP = {'K': 0, 'C': 273.15}

# Create your views here.
def steam_view(request):
    if request.method == 'GET':
        dic = {'ver': VERSION, 'res': False}
        return render(request, 'cal/steam.html', dic)
    elif request.method == 'POST':
        if 'cal' in request.POST:
            prs = request.POST['prs']
            prs2 = float(prs) * float(DIC_PRS[request.POST['uprs']])
            tmp = request.POST['tmp']
            tmp2 = float(tmp) + float(DIC_TMP[request.POST['utmp']])
            stm = request.POST['stm']
            res = WaterHeatCalculation().water_func(prs2, tmp2, stm)
            dic = {'ver': VERSION, 'res': True}
            dic.update(res)
            print(dic)
            return render(request, 'cal/steam.html', dic)
