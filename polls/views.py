from django.shortcuts import render
from django.http import HttpResponse

#create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
