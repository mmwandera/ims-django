from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Asia Tours Agency")

def about(request):
    return HttpResponse("About Asia Tours Agency")