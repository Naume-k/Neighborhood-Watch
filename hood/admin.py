from django.contrib import admin
from .models import NeighbourHood, Profile, Businesses, Posts

# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(Profile)
admin.site.register(Businesses)
admin.site.register(Posts)