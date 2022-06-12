from django.forms.widgets import NullBooleanSelect
from django.http import request
from django.shortcuts import redirect, render
from datetime import datetime,timedelta
from slotbooking.models import Slotbooking
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
import random
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
# from .decorators import admin_only

# Create your views here.

def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context ={'form':form}
    return render(request,'signupslot.html',context)


def ticketbook(request):
    if request.user.is_anonymous:
        return redirect("loginslot")
    user = request.user
    date= datetime.today().date
    print(date)
    slot1= Slotbooking.objects.filter(slots='slot1')
    slot2= Slotbooking.objects.filter(slots='slot2')
    slot3= Slotbooking.objects.filter(slots='slot3')
    print('Slot1:',slot1,len(slot1))
    print('Slot2:',slot2,len(slot2))
    print('Slot3:',slot3,len(slot3))
    remslot1 = 50-len(slot1)
    remslot2 = 50-len(slot2)
    remslot3 = 50-len(slot3)
    date_tommorow=datetime.today().date() + timedelta(days=1)


    if request.method == "POST":
        user = request.user
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        slots = request.POST.get('slots')
        token = str(random.randint(1000000000, 9999999999))

        slotbooking = Slotbooking(token=token,user=user,name=name , email=email , contact =contact , slots=slots , date=datetime.today())
        slotbooking.save()
        template = render_to_string('slotdetail.html',{'name':name,'token':token,'slots':slots,'date':datetime.today().date() + timedelta(days=1)})
        emailmsg = EmailMessage(
            'Hey, '+name+' Your Slot has been booked successfully !',
            template,
            settings.EMAIL_HOST_USER,
            [email],
        )
        emailmsg.fail_silently=False
        emailmsg.send()


        messages.success(request, 'Slot has been Booked ')



    context = {'remslot1':remslot1,'remslot2':remslot2,'remslot3':remslot3,'date_tommorow':date_tommorow}

    return render(request, 'ticketbook.html',context )

def slotlogin(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        # print(username +"" + password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("ticketbook")
    # A backend authenticated the credentials
        else: 
            messages.info(request,'check you username or password')

    # No backend authenticated the credentials

    return render(request, 'login.html')

def logoutUserSlot(request):
    logout(request)
    return redirect('loginslot')

# def adminlogin1(request):
#     if request.method =="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         # print(username +"" + password)
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
            
#             return render(request,'verifyticket.html')
#     # A backend authenticated the credentials
#         else: 
#             messages.info(request,'check you username or password')
#     return render(request,'adminlogin.html')


# def tickets(request):
#     if request.user.is_anonymous:
#         return redirect("loginslot")
#     # user = request.user
#     # print(user)
#     # ticket = Slotbooking.objects.filter(user=user)
#     # print(ticket)


    

#     return render(request,'tickets.html')


class bookedticket(ListView):

    model = Slotbooking
    context_object_name = 'tickets'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tickets'] = context['tickets'].filter(user=self.request.user)
        return context



# @login_required(login_url='loginslot')
# @admin_only
def ticketcheck(request):
    if request.method == "POST":
        ticketno = request.POST.get('ticketno')
        print(ticketno)
        availtickets = Slotbooking.objects.filter(token=ticketno)
        print(availtickets)
        if not availtickets:
            print('not verified please recheck')
            messages.warning(request, 'Not verified please recheck.')
        else:
            print('welcome')
            messages.success(request, 'Welcome to City Mall.')
            Slotbooking.objects.filter(token=ticketno).delete()

    # USE TO CLEAR PREVIOUS DAYS DATA    

    dateslot=Slotbooking.objects.filter(date__lt=datetime.today()).delete()
    print(dateslot)
    print(len(dateslot))


    # slot1= Slotbooking.objects.filter(slots='slot1') 
    # print(slot1)     
        
        


    return render(request,'verifyticket.html')

