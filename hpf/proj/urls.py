# from django.contrib import admin
from unicodedata import name
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('manage/', views.project_management, name="manage"),
    path('donation/', views.donation, name="donation"),
    path("users/", views.user_viewer, name="user_viewer"),
    path("add_facility/", views.add_facility, name="add_facility"),
    path("thanks_for_donating/", views.end_donating, name="end_donating"),
    path("view_facilities/", views.view_facilities, name="view_facilities")
]