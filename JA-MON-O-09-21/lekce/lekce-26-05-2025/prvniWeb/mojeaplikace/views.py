from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

# /pozdrav -> vrati "Ahoj" v html tagu h1
def pozdrav(request):
    message = '<h1>AHOJ</h1>'
    return HttpResponse(message)

# do uvodni stranky pridate odkaz, ktery pujde na /seznam, 
# kde bude vypsany nakupni seznam do obchodu, vyuzijete html tagy ol, li
def seznam(r):
    return render(r, "seznam.html")

# view ktere vygenruje template a vrati seznam uzivatelu pokud existuje
def uzivatele(r):
    users = [
        {"firstname" : "Richard", "lastname" : "Ficek"},
        {"firstname" : "Dominik", "lastname" : "Novak"},
    ]
    return render(r, "users.html", {"users" : users})

# /dynamicSeznam -> vyrenderuje seznam predny jako parametr pri renderovani html souboru
# list = [
#     {"nazev" : "Rohliky", "mnozstni": 10},
#     {"nazev" : "Chleba", "mnozstni": 1},
#     {"nazev" : "Sunka", "mnozstni": 10},
#     {"nazev" : "Mineralka", "mnozstni": 6},
# ]
def dynamicSeznam(r):
    list = [
        {"nazev" : "Rohliky", "mnozstni": 10},
        {"nazev" : "Chleba", "mnozstni": 1},
        {"nazev" : "Sunka", "mnozstni": 10},
        {"nazev" : "Mineralka", "mnozstni": 6},
    ]
    return render(r, "dynamicSeznam.html", {"seznam" : list})

def osloveni(request, jmeno):
    return render(request, "osloveni.html", {"jmeno" : jmeno})

# /test/Richard/24 -> vypisete v html strance Ahoj, {{ jmeno }} {{ vek }} 
def test(request, jmeno, vek):
    return render(request, "jmenoVek.html", {"jmeno": jmeno, "vek":vek})

def formHello(request):
    if request.method == "POST":
        jmeno = request.POST.get("jmeno")
        print(jmeno)
        return render(request, "formAnswer.html", {"jmeno": jmeno})
    return render(request, "form.html")