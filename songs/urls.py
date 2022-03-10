# (2.5 points) As a developer, I want my API to serve content on the following URLs paths: Paths must match these exactly!
# ‘music/' | ‘music/<int:pk>/’

from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.SongsList.as_view()),
    path('music/<int:pk>/', views.SongDetail.as_view()),
]
