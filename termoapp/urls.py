from .views import *
from django.urls import path

app_name = "termoapp"
urlpatterns = [
    path('', home, name="home")
]
