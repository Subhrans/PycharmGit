from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hello world")

def video(request):
    return HttpResponse("this is test video view")