from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

def index(request):
        
        return  render(request, 'index.html')


##done with already 
def counter(request):
        feature1 = Feature()
        feature1.id = 0
        feature1.name = 'Fast'
        feature1.details = "Our service is quicky"
        return render(request, 'counter.html', {'feature': feature1})