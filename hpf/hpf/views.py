# from django.contrib import admin
from unicodedata import name
from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('hpf.urls')),
]