from django.shortcuts import redirect, render
from django.http import JsonResponse

def landingpage(request):

    return render(request,'landingpage.html')