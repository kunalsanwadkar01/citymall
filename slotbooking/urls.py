from django.contrib import admin
from django.urls import path , include
from slotbooking import views

urlpatterns = [
    path("ticketbook/",views.ticketbook , name="ticketbook"),
    path('',views.slotlogin, name="loginslot"),
    path('logoutslot/',views.logoutUserSlot, name="logoutslot"), 
    path('signupslot',views.registerPage,name="signupslot"),
    # path('tickets',views.tickets,name="tickets"),
    path('bookedticket/',views.bookedticket.as_view(),name="bookedticket"),
    path('ticketcheck',views.ticketcheck,name="ticketcheck"),
    # path('adminlogin/',views.adminlogin1,name="adminlogin"),
    





    
]
