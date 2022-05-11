from django.shortcuts import render
from .models import Employes

def index(request):
    data = Employes.objects.all()
    context = {
        'data' : data
    }
    return render(request,
                  template_name='index.html',
                  context=context)
