
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # route for myspots
    # app.com/myspots shows all users spots
    path('myspots/', views.spots_index, name='index'),
    
    # app.com/myspots/create/ lets user create a spot to save
    # route to create a spot
    path('myspots/create/', views.SpotCreate.as_view(), name='spots_create'),
]