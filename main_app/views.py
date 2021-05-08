from django.shortcuts import render, redirect

# import models
from .models import Spot

# class based views
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

def spots_detail(request, spot_id):
    spot = Spot.objects.get(id=spot_id)
    return render(request, 'spots/detail.html', { 'spot': spot })

# delete and update spots
class SpotUpdate(UpdateView):
    model = Spot
    fields = ['title', 'location', 'overview']

class SpotDelete(DeleteView):
    model = Spot
    success_url = '/myspots/'
