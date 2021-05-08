from django.shortcuts import render, redirect

# import models
from .models import Spot, Photo

# class based views
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# needed to upload to s3 buckets
import uuid # helps generate random strings
import boto3 #aws s3 sdk


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