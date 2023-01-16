from django.http import HttpResponse

from datetime import datetime

from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={})
  
def hola_mundo(request):
    return HttpResponse("Hola Mundo!!!")

def fecha_hoy(request):

    hoy = datetime.now().date()
    return HttpResponse(f'La fecha de hoy es es {hoy}')

def emi_template(request):
    return render(request, 'emilia.html', context={})

def caro_template(request):
    return render(request,'caro.html', context={})

  