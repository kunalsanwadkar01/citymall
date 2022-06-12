from django.contrib import admin
from django.urls import path , include
from moviezone import views

urlpatterns = [
    path("",views.moviepage , name="moviezone"),
]
