from django.shortcuts import render
from django.http import HttpResponse
from .urls import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")