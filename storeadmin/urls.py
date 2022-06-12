from django.urls import path
from storeadmin import views

urlpatterns = [
    path('',views.storeadmin,name='storeadmin'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('stadminlogin/',views.storeadminlogin,name="stadminlogin"),
    path('logout/',views.logoutUser,name="logout"),
    path('orders/',views.bookedorders.as_view(),name="bookedorders"),
    path('shipping/',views.shippingdetails.as_view(),name="shippingdetails"),
    path('orderitems/',views.orderitems.as_view(),name="orderitems"),
]
