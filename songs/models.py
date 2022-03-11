# (2.5 points) As a developer, I want to create a Song model. Property names must be in snake_case and match the following exactly!
# title - CharField | artist - CharField | album - CharField | release_date - DateField | genre - CharField

from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=255)
    # this following variable/field is for the bonus user story to add number of "likes"
    likes = models.IntegerField(default=0)
