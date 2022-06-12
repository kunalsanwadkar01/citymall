from django.urls import path

from foodcourt import views

urlpatterns = [
    path('',views.foodcourt,name='foodcourt'),
]
