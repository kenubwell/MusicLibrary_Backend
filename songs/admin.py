from django.contrib import admin
from .models import Song

# this will permit Admin Center interface with our database/table
admin.site.register(Song)
