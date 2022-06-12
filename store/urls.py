from django.urls import path

from store import views

urlpatterns = [
	#Leave as empty string for base url
	path('',views.spmain,name='spmain'),
	path('store', views.store, name="store"),
	path('cart', views.cart, name="cart"),
	path('checkout', views.checkout, name="checkout"),
	path('update_item/',views.updateItem,name="update_item"),
	path('process_order/',views.processOrder,name="process_order"),
	path('pdf_view/',views.ViewPDF.as_view(),name="pdf_view"),

]