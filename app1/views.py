from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app1(request):
    return HttpResponse('<h1>this is first function in app1</h1>')

    
def second(request):
    return HttpResponse('<h1>this is first function in app1</h1>')