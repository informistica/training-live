from django.shortcuts import render,HttpResponse
import datetime

 
def index(request): 
    api_list = ['if','ifelse','elif','for','ifequal','ifnotequal','filter']
    context = {
        'api_list': api_list,
    }
    return render(request, "esempi/index.html", context)
	
def es_if(request):
    #https://www.decodejava.com/django-template-if-tag.htm
    #Creating a dictionary of key-value pairs
    dic = { 'var1' : 200,
    'var2' : 200,
    'var3' : 300 }
    #Calling the render() method to render the request from es_if.html page by using the dictionary, dic
    return render(request, "esempi/es_if.html", dic)

def es_ifelse(request):
    #https://www.decodejava.com/django-template-if-else-tag.htm
    dic = { 'var1' : 100,
    'var2' : 400,
    'var3' : 600 }
    return render(request, "esempi/es_ifelse.html", dic)


def es_for(request):
    #https://www.decodejava.com/django-template-for-tag.htm
    dic = { 'list2': [1, datetime.date(2019,7,16), 'Do not give up!'] }
    return render(request, "esempi/es_for.html", dic)

def es_ifequal(request):
    #https://www.decodejava.com/django-template-for-tag.htm
    dic = { 'list2': [1, datetime.date(2019,7,16), 'Do not give up!'] }
    return render(request, "esempi/es_ifequal.html", dic)

def es_ifnotequal(request):
     #https://www.decodejava.com/django-template-ifnotequal-tag.htm
    dic = { 'var1' : 100,
    'var2' : 100.0,
    'var3' : 100.50,
    'str1' : 'Hello',
    'str2' : 'hello',
    'str3' : "Hello",
    'list1': [1, datetime.date(2019,7,16), 'Make your life productive!'],
    'list2': [2, datetime.date(2019,7,16), 'Do not give up!']}
    return render(request, "esempi/es_ifnotequal.html", dic)

def es_elif(request):
    dic = { 'var1' : 100,
    'var2' : 100.0,
    'var3' : 100.50,
    'str1' : 'Hello',
    'str2' : 'hello',
    'str3' : "Hello",
    'list1': [1, datetime.date(2019,7,16), 'Make your life productive!'],
    'list2': [2, datetime.date(2019,7,16), 'Do not give up!']}
    return render(request, "esempi/es_elif.html", dic)

def es_filter(request):
    dic = { 'list2': [1, datetime.date(2019,7,16), 'Do not give up!'] }
    return render(request, "esempi/es_filter.html", dic)
