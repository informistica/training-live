from django.shortcuts import render,HttpResponse
import datetime
from .forms import FormContatto

 
def index(request): 
    api_list = ['if','ifelse','elif','for','ifequal','ifnotequal','filter','form']
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
    dic = { 'var1' : 'admin',
    'var2' : 'admin',
    'var3' : 600 }
    return render(request, "esempi/es_ifelse.html", dic)


def es_for(request):
    #https://www.decodejava.com/django-template-for-tag.htm
    dic = { 'list1': [1, datetime.date(2019,7,16), 'Do not give up!'],'list2': [1, datetime.date(2019,7,16), 'Do not give up!'] }
    return render(request, "esempi/es_for.html", dic)

def es_ifequal(request):
    #https://www.decodejava.com/django-template-for-tag.htm
    dic = { 'list1': [1, datetime.date(2019,7,16), 'Do not give up!'],'list2': [1, datetime.date(2019,7,16), 'Do not give up!'],'str1':'admin','str2':'admin' }
  
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

def es_form(request):
    # form = FormContatto()
    # context={"form": form}
    # return render(request, "esempi/es_form.html", context)

# Se la richiesta è di tipo POST, allora possiamo processare i dati
    if request.method == "POST":
        # Creiamo l'istanza del form e la popoliamo con i dati della POST request (processo di "binding")
        form = FormContatto(request.POST)

        # is_valid() controlla se il form inserito è valido:
        if form.is_valid():
            # a questo punto possiamo usare i dati validi!
            # tenere a mente che cleaned_data["nome_dato"] ci permette di accedere ai dati validati e convertiti in tipi standard di Python
            print("Il Form è Valido!")
            print("NOME: ", form.cleaned_data["nome"])
            print("COGNOME: ", form.cleaned_data["cognome"])
            print("EMAIL: ", form.cleaned_data["email"])
            print("CONTENUTO: ", form.cleaned_data["contenuto"])

            #   volendo possiamo effettuare un redirect a una pagina specifica
            return HttpResponse("<h1>Grazie per averci contattato!</h1>")

    # Se la richiesta HTTP usa il metodo GET o qualsiasi altro metodo, allora creo invece il form di default
    else:
        form = FormContatto()

    # arriviamo a questo punto se si tratta della prima volta che la pagina viene richiesta(con metodo GET), o se il form non è valido e ha errori
    context = {"form": form}
    return render(request, "esempi/es_form.html", context)
