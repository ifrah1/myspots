from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

# Create your views here.

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello Test</h1>')