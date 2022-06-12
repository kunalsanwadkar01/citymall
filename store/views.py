from django import template
from django.shortcuts import render
from .models import *
from django.http import JsonResponse,HttpResponse
import json
import datetime
from . utils import cookieCart,cartData,guestOrder
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View

# Create your views here.
def render_to_pdf(template_src,context_dict={}):
    template= get_template(template_src)
    html= template.render(context_dict)
    result=BytesIO()
    pdf= pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None

data={
    "company":"test",
    "zip":"123",
}

class ViewPDF(View):
    def get(self,request,*args,**kwargs):
        data = cartData(request)
        cartItems = data['cartItems']
        order = data['order']
        items = data['items']
        
        
        
        context = {'items':items , 'order':order,'cartItems':cartItems}

        pdf = render_to_pdf('app/pdf_template.html',context)
        return HttpResponse(pdf, content_type='application/pdf')

def spmain(request):
    
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        contact = request.POST.get('contact')
        emailid = request.POST.get('emailid')

        print(fname)
    
    
    return render(request,'shopping.html')

def store(request):

    data = cartData(request)
    cartItems = data['cartItems']
    
        

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store.html', context)

def cart(request):
    

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

        
        
    context = {'items':items , 'order':order,'cartItems':cartItems}
    return render(request, 'cart.html', context)

def checkout(request):
	
    
        
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
        
        
        
    context = {'items':items , 'order':order,'cartItems':cartItems}
    return render(request, 'checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId= data['productId']
    action= data['action']

    print(productId + action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)

def processOrder(request):
    print('Data:',request.body)
    data= json.loads(request.body)
    transaction_id= datetime.datetime.now().timestamp()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        

       
    else:
        customer, order = guestOrder(request , data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()  

    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        )     
    return JsonResponse('payment Done',safe=False)