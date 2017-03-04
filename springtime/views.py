from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #This should change to return the index page
    return render(request, 'springtime/main.html')