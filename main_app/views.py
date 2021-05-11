from django.shortcuts import render, redirect

# import models
from .models import Spot, Photo

# class based views
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# needed to upload to s3 buckets
import uuid # helps generate random strings
import boto3 #aws s3 sdk

# to show map need folium
import folium


# variables needed for s4 buckets
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'armyspots'

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

    context = {
        'spots': spots,
    }

    return render(request, 'spots/index.html',context)

# create a spot
class SpotCreate(CreateView):
    model = Spot
    # fields = '__all__'
    fields = ['title','location','overview', 'longitude', 'latitude']

# display a single spot
def spots_detail(request, spot_id):
    spot = Spot.objects.get(id=spot_id)

    # logic to show map 
    m = folium.Map(location=[spot.latitude,spot.longitude], zoom_start=17)
    # add map marker 
    folium.Marker([spot.latitude,spot.longitude], tooltip='Click for info', popup=spot.location).add_to(m)

    #add tiles to map
    folium.raster_layers.TileLayer('Open Street Map').add_to(m)
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
    folium.LayerControl().add_to(m)

    # change map object to a html
    m = m._repr_html_()
    #-------

    context = {
        'spot': spot,
        'm': m
    }
    return render(request, 'spots/detail.html', context)

# delete and update spots
class SpotUpdate(UpdateView):
    model = Spot
    fields = ['title', 'location', 'overview']

class SpotDelete(DeleteView):
    model = Spot
    success_url = '/myspots/'

# adds a photo to s3 buckets 
def add_photo(request, spot_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to spot_id or spot (if you have a spot object)
            photo = Photo(url=url, spot_id=spot_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', spot_id=spot_id)


def map_view(request):
    spots = Spot.objects.all()
    # print(spots)
    # logic to show map 
    m = folium.Map(location=[34.77764421466408,-55.5343331753092], zoom_start=4)
    
    # # add map marker 
    for spot in spots:
        # print(spot.id)
        aTag = f'<a href="/myspots/{spot.id}" target="_blank">{spot.title}</a> <br> {spot.overview}'
        # setup popup size and info
        popup = folium.Popup(aTag, max_width=400)
        # print(aTag)
        folium.Marker([spot.latitude,spot.longitude], tooltip='Click for info', popup=popup).add_to(m)

    #add tiles to map
    folium.raster_layers.TileLayer('Open Street Map').add_to(m)
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
    folium.LayerControl().add_to(m)

    # change map object to a html
    m = m._repr_html_()
    #-------
    context = {
        'm': m
    }

    return render(request, 'map.html', context)