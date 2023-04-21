from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    
    response = render(request,'Homeapp/home_views.html')
    return HttpResponse(response)

def sign_up_view(request):
    
    response = render(request,'Homeapp/signup_views.html')
    return HttpResponse(response)


def login_view(request):
    
    response = render(request,'Homeapp/login_views.html')
    return HttpResponse(response)