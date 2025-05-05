from flask import Flask, request, render_template, redirect, url_for, abort, send_file
import io

app = Flask(__name__)

# 1. Základní routy (Routes)
@app.route('/')
def home():
    # Hlavní stránka – zde by se zobrazovala úvodní stránka aplikace
    return render_template('index.html')

@app.route('/about')
def about():
    # Stránka "O nás" – informace o projektu nebo autorovi
    # vratime text: "Autor: Richard Ficek"
    return "Autor: Richard Ficek"

# 2. Dynamické routy
@app.route('/user/<username>')
def show_user(username):
    # Dynamická stránka pro uživatele podle jména
    # vratime text s podravem podle jmena
    return f"Ahoj, {username}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Dynamická stránka pro příspěvek podle ID (čísla)
    # vypise text 
    # "Prispevek cislo 1" url -> /post/1
    # "Prispevek cislo 2" url -> /post/2
    # "Prispevek cislo 999" url -> /post/999
    text = "Příspěvek číslo " + str(post_id)
    return text

@app.route('/category/<category>')
def show_category(category):
    # Dynamická stránka pro kategorii podle názvu
    # "kategori ma nazev PC" -> /category/PC
    # "kategori ma nazev Auto" -> /category/Auto
    return f'Kategorie: {category}'

# 3. HTTP metody (GET, POST)
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Přihlašovací stránka – GET zobrazí formulář, POST zpracuje přihlášení
    if request.method == 'POST':
        return "Zpracovani prihlaseni"
    else:
        return "Prihlasovaci formular"

# 4. Templates (Šablony)
@app.route('/hello/<name>')
def hello(name):
    # Ukázka použití šablony s proměnnou (např. hello.html)
    return render_template("hello.html", name=name, title="TEST")

# 5. Zpracování formulářů
@app.route('/form', methods=['GET', 'POST'])
def form():
    # Stránka s formulářem – GET zobrazí, POST zpracuje data z formuláře
    if request.method == 'POST':
        name = request.form['name']
        # return render_template("hello.html", name=name)
        # return redirect(url_for('home'))
        
    else:
        return '''
<form method="post">
    <label for="name">Jmeno: </label>
    <input type="text" name="name">
    <button type="submit">Posli na server</button>
</form>
'''
        # return render_template("test.html")

# 6. Redirecty a chyby
@app.route('/redirect')
def redirect_example():
    # Přesměrování na jinou stránku v aplikaci
    return redirect(url_for('form'))

@app.route('/error')
def error_example():
    # Vyvolání chyby 404 – stránka nenalezena
    abort(404)

# Vlastní stránka pro chybu 404
@app.errorhandler(404)
def page_not_found(e):
    # Vlastní text nebo stránka pro chybu 404
    return "Nastala chyba pri presmerovani", 404


# Vlastní stránka pro chybu 404
@app.errorhandler(500)
def page_not_exist(e):
    # Vlastní text nebo stránka pro chybu 404
    return "Pozadovana stranka nebyla nalezena", 500

# 7. Vrácení různých typů odpovědí

@app.route('/text')
def text_response():
    # Vrácení čistého textu
    return "Toto je textová odpověď"

@app.route('/html')
def html_response():
    # Vrácení HTML kódu
    # nadpi a nejaky text, --> html tagy h2, p
    return "<h2>HTML odpověď</h2><p>Toto je odstavec v HTML.</p>"

@app.route('/json')
def json_response():
    # Vrácení JSON odpovědi (např. slovník)
    # { "status" : "ok", "text" : "Ahoj svete", "kod" : 200}
    return { "status" : "ok", "text" : "Ahoj svete", "kod" : 200}

@app.route('/tuple')
def tuple_response():
    # Vrácení odpovědi jako tuple (obsah, status kód, hlavičky)
    # tuple --> ("Hodnota", 202, { "text" : "Ahoj svete jak se mas"})
    return ("Hodnota", 202, { "text" : "Ahoj svete jak se mas"})

# 8. Vrácení souboru ke stažení
@app.route('/download')
def download_file():
    # Vrácení souboru ke stažení (např. textový soubor)
    # Vytvoří soubor v paměti a nabídne ke stažení
    file_content = "Toto je obsah souboru."
    return send_file(
        io.BytesIO(file_content.encode()),
        mimetype='text/plain',
        as_attachment=True,
        download_name='soubor.txt'
    )

# 9. Vrácení přesměrování na externí web
@app.route('/google')
def google_redirect():
    # Přesměrování na externí web (např. Google)
    # https://www.google.com/ --> sem se dostanu po zavolani endpointu /google
    return redirect("https://www.google.com")

# 10. Vlastní HTTP status kód a hlavičky
@app.route('/custom')
def custom_response():
    # Vrácení odpovědi s vlastním status kódem a hlavičkami
    response = app.response_class(
        response="Tohle je ma odpoved",
        status=201,
        headers={"X-Example": "Test"}
    )
    return response

@app.route('/styled')
def styled():
    # Vrácení HTML stránky s vloženým CSS stylem
    # vratit webovou stranku, kde nadpis bude cerveny text bude modry, a body bude sedy
    # pokus je vraceni html kodu primo
    # return '''
    # <html>
    #   <head>
    #     <style>
    #       body { background: gray; }
    #       h1 { color: red; }
    #       p { color: blue; }
    #     </style>
    #   </head>
    #   <body>
    #     <h1>Stylovaná stránka</h1>
    #     <p>Toto je stránka s vloženým CSS.</p>
    #   </body>
    # </html>
    # '''
    # pokus 2. vygenerovani stranky
    return render_template("style.html")

@app.route('/plain')
def plain():
    # Vrácení čistého textu s nastaveným content-type
    return "Cisty text", 200, {"Content-type": "text/plain" }

@app.route('/headers')
def headers():
    # Vrácení odpovědi s vlastními hlavičkami
    return ("Odpověď s hlavičkami", 200, {
        "X-First": "Jedna",
        "X-Second": "Dva"
    })

@app.route('/xml')
def xml():
    # Vrácení XML odpovědi
    xml_data = "<note><to>User</to><body>Ahoj!</body></note>"
    return xml_data, 200, {'Content-Type': 'application/xml'}

@app.route('/csv')
def csv():
    # Vrácení CSV dat
    csv_data = "jmeno,vek\nPetr,30\nAnna,25"
    return csv_data, 200, {'Content-Type': 'text/csv'}

@app.route('/set-cookie')
def set_cookie():
    # Nastaví cookie v odpovědi
    resp = app.make_response("Cookie nastaveno")
    resp.set_cookie('moje_cookie', 'Tohle je muj tajny a sledovaci kod')
    return resp

@app.route('/get-cookie')
def get_cookie():
    # Získá hodnotu cookie
    value = request.cookies.get('moje_cookie', 'nenastaveno')
    return f'Hodnota cookie: {value}'

@app.route('/status')
def status():
    # Vrácení pouze status kódu bez obsahu (např. 204)
    return '', 203

@app.route('/json-list')
def json_list():
    # Vrácení JSON pole (seznam slovníků)
    json = [{ "status" : "ok", "text" : "Ahoj svete", "kod" : 200},{ "status" : "ok", "text" : "Ahoj svete", "kod" : 200} ]
    return json

@app.route('/json-nested')
def json_nested():
    # Vrácení vnořeného JSON (slovník v slovníku)
    json = [{ "status" : "ok", "text" : "Ahoj svete", "kod" : 200, "jsonfile" : { "status" : "ok", "text" : "Ahoj svete", "kod" : 200}},{ "status" : "ok", "text" : "Ahoj svete", "kod" : 200} ]
    return json

@app.route('/html-table')
def html_table():
    # Vrácení HTML stránky s tabulkou
    # html tagy --> table, tr, th, td
    # jednoducha tabulka o dvou radcich

    # vracim pouze dany kus html
    # return '''
    # <table border="1">
    #   <tr><th>Jméno</th><th>Věk</th></tr>
    #   <tr><td>Petr</td><td>30</td></tr>
    #   <tr><td>Anna</td><td>25</td></tr>
    # </table>
    # '''

    # vracim vyrenderovanou stranku 
    return render_template("table.html")

@app.route('/inline-js')
def inline_js():
    # Vrácení HTML stránky s JavaScriptem
    #  html tagy -> button, h2
    # javascript -> by mel otevrit popup okno (vyskakovaci okno)
    # return '''
    # <html>
    #   <body>
    #     <h2>Ukázka JavaScriptu</h2>
    #     <button onclick="alert('Ahoj ze Flasku!')">Klikni mě</button>
    #   </body>
    # </html>
    # '''
    return render_template("inlineJS.html")

@app.route('/inline-img')
def inline_img():
    # Vrácení HTML stránky s obrázkem
    return '''
    <html>
      <body>
        <h2>Obrázek</h2>
        <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python logo" width="200">
      </body>
    </html>
    '''

@app.route('/params')
def params():
    # Vrácení GET parametrů z URL
    args = dict(request.args)
    return f'Parametry v URL: {args}'
    

@app.route('/post-json', methods=['POST'])
def post_json():
    # Přijetí a vrácení JSON dat v POST požadavku
    data = request.get_json()
    return {"Obdrzel" : data}

@app.route('/uppercase/<text>')
def uppercase(text):
    # Vrácení textu převedeného na velká písmena
    # return text.lower()
    return text.upper()

@app.route('/repeat/<int:n>/<word>')
def repeat(n, word):
    # Vrácení slova opakovaného n-krát
    text = word * n
    return text

if __name__ == '__main__':
    app.run(debug=True)