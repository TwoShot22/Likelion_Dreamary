from django.shortcuts import render
from .models import Info

# Create your views here.
def home(request):
    return render(request, 'home.html')

def introduce(request):
    return render(request, 'introduce.html')

def new(request):
    return render(request, 'new.html')