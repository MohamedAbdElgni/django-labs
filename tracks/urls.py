from django.urls import path, include
from .views import *
urlpatterns = [
    
    path('',  Tracks ,name='Tracks',),
    path('<int:id>/',   TrackDetails ,name='TrackDetails',),
]
