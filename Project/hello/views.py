from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def jamie(request):
   return HttpResponse("Hello, jamie!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
def htmlfunc(request):
    now = datetime.datetime.now()
    return render(request, "hello/index.html", {
        "newyear": now.month == 1 and now.day == 1})