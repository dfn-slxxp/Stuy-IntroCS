from django.shortcuts import render
from .farms import renderFarms, newFarm

# Create your views here.
def home(request):
    return render(request, "home.html")

def submit(request):
    return newFarm(request)

def farms(request):
    return renderFarms(request)