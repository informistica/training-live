from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64
import urllib.request, json, pprint
from django.http import JsonResponse

numstud = 0
numperiodi = 0
listaPeriodi = []

Pdict = {}  # dizionario nomestudente -> numero
Inpdict = {}  # numero -> nomestudente
StudPos = {}  # nomestudente -> lista delle posizioni in classifica nei vari periodi
StudPunti = {}  # nomestudente -> lista dei punti nei vari periodi
StudVoti = {}  # nomestudente -> lista dei voti nei vari periodi
StudMedia = {}  # nomestudente -> media dei voti nei vari periodi
Periodi = []  # lista dei periodi da mostrare

# lista dei colori per i grafici
Col = ["Black", "Red", "Green", "Blue", "Magenta", "Black", "Red", "Green", "Blue", "Magenta"]
# lista dei marcatori per lo stile del grafico
Mrk = ["s", "o", "^", "D"]
plt.rcParams['figure.figsize'] = 12, 9
plt.rcParams['figure.autolayout'] = True


def home(request):
    return render(request, "matplot/home.html")


def myplot(playerlist, numperiodi, idxCol, idxMrk):
    for p in playerlist:
        # print("sono in myplot")
        # print(idxCol)
        # print(idxMrk)
        plt.plot(StudVoti[p], c=Col[idxCol], ls='--', marker=Mrk[idxMrk], ms=7, label=p)
        plt.xticks(list(range(0, numperiodi + 1)), Periodi, rotation='vertical')
        # plt.yticks(list(range(0,9)), list(range(0,9)), rotation='horizontal')
        plt.legend(loc='upper left',
                   bbox_to_anchor=(1, 1))  # loc- which corner of the legend to use, bbox- where to put it
        idxCol += 1
        if idxCol == 10:
            idxCol = 0
        idxMrk += 1
        if idxMrk == 4:
            idxMrk = 0
    return plt


def mostraclassi(request, id_classe, periodo):
    # periodo=0 fine anno =1 recupero a settembre'
    listaGrafici = []
    myplayer = []
    Studenti = []  # lista degli studenti
    idxCol = 0
    idxMrk = 0
    if periodo == 0:
        link = "https://www.umanetexpo.net/expo2015Server/UECDL/grafici/as_1920/report&" + id_classe + ".json"
    elif periodo == 1:
        link = "https://www.umanetexpo.net/expo2015Server/UECDL/grafici/as_1920/report&" + id_classe + "_recupero.json"

    # link="https://www.umanetexpo.net/expo2015Server/UECDL/script/cClasse/classifica_report_json.asp?classe=5Ct$6&id_classe=28COM"
    with urllib.request.urlopen(link) as url:
        stud_dict = json.loads(url.read().decode())
    intestazione = stud_dict['intestazione']
    risultati = stud_dict['risultati']
    listaPeriodi = intestazione.split("&")
    numperiodi = len(listaPeriodi) - 3
    # print("numperiodi:" + str(numperiodi))
    # print("numstud:" + str(len(risultati)))

    numStud = len(risultati)
    for i in range(2, 2 + numperiodi):
        Periodi.append([listaPeriodi[i]])  # aggiungo i periodi

    # Popolo la lista degli studenti e i due dizionari di supporto
    for i, stud in enumerate(risultati):
        Studenti.append(stud[0].replace(' ', ''))
        Pdict[stud[0].replace(' ', '')] = i
        Inpdict[i] = stud[0].replace(' ', '')

    # popolo i dizionari delle posizioni, voti, punti
    for s in range(0, numStud):
        StudPos[Inpdict[s]] = []
        StudVoti[Inpdict[s]] = []
        StudPunti[Inpdict[s]] = []
        StudMedia[Inpdict[s]] = []

    for i, stud in enumerate(risultati):
        k = 0
        j = 0
        for j, dati in enumerate(stud):
            if j == 0:
                # print("studente:"+dati)
                j = 1
            else:
                if k == 0:
                    StudPos[Inpdict[i]].append(float(dati))
                if k == 1:
                    StudVoti[Inpdict[i]].append(float(dati))
                if k == 2:
                    StudPunti[Inpdict[i]].append(float(dati))
                k += 1
                if k == 3:
                    k = 0
                if j == len(risultati):
                    StudMedia[Inpdict[i]].append(float(dati))

    # pprint.pprint(StudPos)
    # pprint.pprint(StudVoti)
    # pprint.pprint(StudPunti)
    i = 0
    finito = False

    while (not finito):
        if i < len(Studenti):
            myplayer.append(Studenti[i])
        else:
            finito = True
            pass
        if i + 1 < len(Studenti):
            myplayer.append(Studenti[i + 1])
        else:
            finito = True
            pass
        if i + 2 < len(Studenti):
            myplayer.append(Studenti[i + 2])
        else:
            finito = True
            pass
        if i + 3 < len(Studenti):
            myplayer.append(Studenti[i + 3])
        else:
            finito = True
            pass
        if i + 4 < len(Studenti):
            myplayer.append(Studenti[i + 4])
        else:
            finito = True
            pass
        i += 5
        print(myplayer)
        plot = myplot(myplayer, numperiodi, idxCol, idxMrk)
        del myplayer[0:len(myplayer)]
        fig = plot.gcf()
        # convert graph into dtring buffer and then we convert 64 bit code into image
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        listaGrafici.append(uri)
        plt.close()
        classe, anno = id_classe.split("$")
    return render(request, 'matplot/grafici.html',
                  {'data': listaGrafici, 'studenti': Studenti, 'id_classe': id_classe, 'classe': classe})


def mostragruppi(request, id_classe):
    periodo = 0
    # pass
    print("chiamata")
    # periodo=0 fine anno =1 recupero a settembre'
    response_data = {}
    if request.POST.get('action') == 'post':
        listaGrafici = []
        myplayer = []
        Studenti = []  # lista degli studenti
        idxCol = 0
        idxMrk = 0
        if periodo == 0:
            link = "https://www.umanetexpo.net/expo2015Server/UECDL/grafici/as_1920/report&" + id_classe + ".json"
        elif periodo == 1:
            link = "https://www.umanetexpo.net/expo2015Server/UECDL/grafici/as_1920/report&" + id_classe + "_recupero.json"

        # link="https://www.umanetexpo.net/expo2015Server/UECDL/script/cClasse/classifica_report_json.asp?classe=5Ct$6&id_classe=28COM"
        with urllib.request.urlopen(link) as url:
            stud_dict = json.loads(url.read().decode())
        intestazione = stud_dict['intestazione']
        risultati = stud_dict['risultati']
        listaPeriodi = intestazione.split("&")
        numperiodi = len(listaPeriodi) - 3
        numStud = len(risultati)
        for i in range(2, 2 + numperiodi):
            Periodi.append([listaPeriodi[i]])  # aggiungo i periodi

        # Popolo la lista degli studenti e i due dizionari di supporto
        for i, stud in enumerate(risultati):
            Studenti.append(stud[0].replace(' ', ''))
            Pdict[stud[0].replace(' ', '')] = i
            Inpdict[i] = stud[0].replace(' ', '')

        # popolo i dizionari delle posizioni, voti, punti
        for s in range(0, numStud):
            StudPos[Inpdict[s]] = []
            StudVoti[Inpdict[s]] = []
            StudPunti[Inpdict[s]] = []
            StudMedia[Inpdict[s]] = []

        for i, stud in enumerate(risultati):
            k = 0
            j = 0
            for j, dati in enumerate(stud):
                if j == 0:
                    # print("studente:"+dati)
                    j = 1
                else:
                    if k == 0:
                        StudPos[Inpdict[i]].append(float(dati))
                    if k == 1:
                        StudVoti[Inpdict[i]].append(float(dati))
                    if k == 2:
                        StudPunti[Inpdict[i]].append(float(dati))
                    k += 1
                    if k == 3:
                        k = 0
                    if j == len(risultati):
                        StudMedia[Inpdict[i]].append(float(dati))

        txtStud = request.POST.get('description')

        listas = txtStud.split(',')
        # listas=[0,1]
        for i in listas:
            myplayer.append(Inpdict[int(i) - 1])
        print(myplayer)
        plot = myplot(myplayer, numperiodi, idxCol, idxMrk)
        del myplayer[0:len(myplayer)]
        fig = plot.gcf()
        # convert graph into dtring buffer and then we convert 64 bit code into image
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        response_data['uri'] = uri
        response_data['classe'] = id_classe
        # listaGrafici.append(uri)
        plt.close()
        return JsonResponse(response_data)

    # return render(request, 'grafici.html', {'data': uri, 'studenti': Studenti, 'id_classe': id_classe})
