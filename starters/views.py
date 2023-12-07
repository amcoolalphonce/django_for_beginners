from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

def index(request):
        feature1 = Feature()
        feature1.id = 0
        feature1.name = 'Fast'
        feature1.details = "Our service is quicky"
        return  render(request, 'index.html', {'feature ': feature1})


##done with already 
def counter(request):
        text = request.POST['text']
        amount_of_words = len(text.split())
        return render(request, 'counter.h tml', {'amount': amount_of_words})