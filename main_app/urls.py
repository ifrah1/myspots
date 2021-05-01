
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # route for myspots
    # app.com/myspots shows all users spots
    # app.com/myspots/create/ lets user create a spot to save
    
]