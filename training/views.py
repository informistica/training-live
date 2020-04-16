from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request): 
    blog_command = ['esempi','blog']
    context = {
        'menu': blog_command,
    }
    return render(request, "index.html", context)
