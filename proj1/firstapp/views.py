from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    s='<h1>i am software engineer</h1>'
    return HttpResponse(s)