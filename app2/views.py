from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app2(request):
    return HttpResponse('<h1>this is first function in app2</h1>')