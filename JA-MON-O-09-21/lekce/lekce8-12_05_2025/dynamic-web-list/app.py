"""
Ukázková Flask aplikace – základy dynamického webu

Tento soubor ukazuje, jak:
- vytvořit různé stránky (routy) ve Flasku,
- předávat proměnné do šablon,
- pracovat s cykly a podmínkami v šablonách,
- zpracovávat formuláře,
- používat parametry v URL.

Každá route (funkce s @app.route) odpovídá jedné stránce webu.
"""

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    # Úvodní stránka s odkazy na ukázky
    return render_template('index.html')

@app.route('/pozdrav')
def pozdrav():
    # Ukázka vkládání proměnné do šablony
    # Do šablony pozdrav.html pošleme proměnnou jmeno s hodnotou 'Anna' 
    return render_template('pozdrav.html', jmeno='Richard')

@app.route('/uzivatele')
def uzivatele():
    # Ukázka výpisu seznamu a podmínky
    # Do šablony uzivatele.html pošleme seznam uživatelů
    users = ["Anna", "Petr", "Jana"]
    return render_template('uzivatele.html', users=users)

@app.route('/tabulka')
def tabulka():
    # Ukázka generování tabulky z dat
    # Do šablony tabulka.html pošleme seznam slovníků (osoby)
    osoby = [{"jmeno": "Anna", "vek": 23}, {"jmeno": "Petr", "vek": 31}, {"jmeno": "Pavel", "vek": 18}]
    return render_template('tabulka.html', osoby=osoby)

@app.route('/dotaz', methods=['GET', 'POST'])
def dotaz():
    # Ukázka formuláře a zpracování dat
    # GET: zobrazí formulář (dotaz.html)
    # POST: zpracuje data z formuláře a zobrazí výsledek (vysledek.html)
    print(request.form)
    if request.method == "POST":
        return render_template("vysledek.html", odpoved=request.form["odpoved"])
    elif request.method == "GET":
        return render_template("dotaz.html")
    else:
        return redirect("/")

@app.route('/pozdrav/<jmeno>')
def pozdrav_param(jmeno):
    # Ukázka práce s parametrem v URL
    # Hodnota <jmeno> z adresy se pošle do šablony pozdrav.html
    return render_template("pozdrav.html", jmeno=jmeno)

# Sablonu v about.html, ktera budu obrasahovat vase jmeno, prijmeni a vek 
# -> vse se bude predavat jako samostana promenna
@app.route("/about")
def about():
    jmeno = "Richard"
    prijmeni = "Ficek"
    vek = 24
    return render_template("about.html", jmeno=jmeno, vek=vek, prijmeni=prijmeni)


if __name__ == '__main__':
    # Spuštění aplikace v režimu debug (vhodné pro vývoj)
    app.run(debug=True)