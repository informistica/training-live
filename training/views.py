from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request): 
    applicazioni = ['esempi','blog','plot']
    context = {
        'menu': applicazioni,
    }
    return render(request, "index.html", context)
