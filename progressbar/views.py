from django.shortcuts import render
from time import sleep

# Create your views here.

def index(request):
    sleep(6)
    return render(request, 'progressbar/index.html')