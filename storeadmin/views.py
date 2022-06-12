from django.db.models.fields.related import ForeignKey
from django.shortcuts import redirect, render
from django.http import JsonResponse
from store.models import *
from django.core.files.images import get_image_dimensions
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import admin_only, allowed_users, unauthenticated_user
from django.views.generic.list import ListView
# Create your views here.

@unauthenticated_user
def storeadminlogin(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('addproduct')
        else:
            messages.info(request,'check you username or password')
            
    
    
    return render(request,'stadminlogin.html')

def logoutUser(request):
    logout(request)
    return redirect('stadminlogin')


def storeadmin(request):
    products = Product.objects.all()
    order = Order.objects.filter(complete=True)
    

    
    # for i in order:
    #     productorder = OrderItem.objects.filter(order=i)
    #     print(i)
        

        
        
    
    
    print(products)
    context = {'products':products,'order':order}

    return render(request,'storeadmin.html',context)

@login_required(login_url='stadminlogin')
@admin_only
def addproduct(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        size = request.POST.get('size')
        productimg = request.POST.get('productimg')
        # w,h = get_image_dimensions(productimg)
        # if w != 330:
        #     raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 330px" % w)
        # elif h !=180:
        #     raise forms.ValidationError("The image is %i pixel high. It's supposed to be 180px" % h)
        products =Product(name=name, price=price, size=size, image=productimg )
        products.save() 
    context={}
    return render(request,'addproduct.html',context)

@login_required(login_url='stadminlogin')
@admin_only
def orders(request):
    

    return render(request,'orders.html')

class bookedorders(ListView):

    model = Order
    context_object_name = 'orders'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = context['orders']
        return context

    
    

class shippingdetails(ListView):

    model = ShippingAddress
    context_object_name = 'shipping'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shipping'] = context['shipping']
        return context



class orderitems(ListView):

    model = OrderItem
    context_object_name = 'ordereditems'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordereditems'] = context['ordereditems']
        #context1['ordereditems'] = context1['ordereditems']
        return context
