from django.http import HttpResponse
from django.shortcuts import redirect
from slotbooking import urls
from django.contrib.auth import logout
from django.contrib import messages



def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            logout(request)
            messages.warning(request, 'You are not authorized to view this page')
            return redirect('login')

        


        if group == 'admin':
            return view_func(request, *args, **kwargs)
    
    return wrapper_function