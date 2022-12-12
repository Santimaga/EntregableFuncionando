from django.urls import path
from .views import *

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path('familia/', familiar, name='familia'),
]