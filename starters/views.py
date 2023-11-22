from django.shortcuts import render
from django.http import HttpResponse

def index(request):
        name = 'Amcool'
        return  render(request, 'index.html', {'name': name})