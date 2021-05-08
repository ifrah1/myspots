from django.shortcuts import render, redirect

# import models
from .models import Spot

# class based views
from django.views.generic.edit import CreateView

# Create your views here.

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# view all spots
def spots_index(request):
    # spots = Spot.objects.filter(user=request.user)
    spots = Spot.objects.all()
    return render(request, 'spots/index.html', {'spots': spots})

# create a spot
class SpotCreate(CreateView):
    model = Spot
    # fields = '__all__'
    fields = ['title','location','overview', 'longitude', 'latitude']