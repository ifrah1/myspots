
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

    # app.com/myspots/:spot_id/ route for a single spot
    # route to see detail of a spot
    path('myspots/<int:spot_id>/', views.spots_detail, name='detail'),

    # delete and update route
    path('myspots/<int:pk>/update/', views.SpotUpdate.as_view(), name='spots_update'),
    path('myspots/<int:pk>/delete/', views.SpotDelete.as_view(), name='spots_delete'),

    # add photo route
    path('myspots/<int:spot_id>/add_photo/', views.add_photo, name='add_photo'),

    # map view of my spot
    path('myspots/map/', views.map_view, name='map'),

    # path to sign up a new user
    path('accounts/signup/', views.signup, name='signup'),

]