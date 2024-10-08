from django.urls import path
from .views import fetch_albums

urlpatterns = [
    path('albums/', fetch_albums, name='fetch_albums')
]
