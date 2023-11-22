from django.shortcuts import render
from django.http import HttpResponse

def index(request):
        context = {
                'name' : 'Amcool',
                'age' : '22',
        }
        return  render(request, 'index.html', {'name': name})