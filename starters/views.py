from django.shortcuts import render
from django.http import HttpResponse

def index(request):
        context = { }
        return  render(request, 'index.html', context)

def counter(request):
        text = request.GET['text']
        amount_of_words = len(text.split())
        return render(request, 'counter.html', {'amount': amount_of_words})