from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request):
    return HttpResponse('About')

def login(request):
    return HttpResponse('Page login')

def contacts(request):
    return HttpResponse('Page contacts')