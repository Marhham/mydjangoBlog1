from django.shortcuts import render
from . import models

# Create your views here.
def tabe(request):
    degisken = models.Article.objects.all().order_by('body')

    args =  {'esm':degisken}
    return render(request ,'app/tabe.html', args)
