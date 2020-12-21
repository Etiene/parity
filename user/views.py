from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("See user")


def update(request):
    return HttpResponse("Update user")


def register(request):
    return HttpResponse("Create new user")
