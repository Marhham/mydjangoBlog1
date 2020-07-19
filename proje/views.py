from django.shortcuts import render
from django.shortcuts import HttpResponse


def hmhm(request):
    return HttpResponse('salammmmmmmmm')
def home(request):
    return render(request , 'home.html')
