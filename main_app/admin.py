from django.contrib import admin


# import models here
from .models import Spot, Photo

# Register your models here.
admin.site.register(Spot)
admin.site.register(Photo)