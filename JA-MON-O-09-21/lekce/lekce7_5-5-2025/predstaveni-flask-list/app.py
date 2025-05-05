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
    return render_template("hello.html", name=name)

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
    pass

@app.route('/html')
def html_response():
    # Vrácení HTML kódu
    pass

@app.route('/json')
def json_response():
    # Vrácení JSON odpovědi (např. slovník)
    pass

@app.route('/tuple')
def tuple_response():
    # Vrácení odpovědi jako tuple (obsah, status kód, hlavičky)
    pass

# 8. Vrácení souboru ke stažení
@app.route('/download')
def download_file():
    # Vrácení souboru ke stažení (např. textový soubor)
    pass

# 9. Vrácení přesměrování na externí web
@app.route('/google')
def google_redirect():
    # Přesměrování na externí web (např. Google)
    pass

# 10. Vlastní HTTP status kód a hlavičky
@app.route('/custom')
def custom_response():
    # Vrácení odpovědi s vlastním status kódem a hlavičkami
    pass

@app.route('/styled')
def styled():
    # Vrácení HTML stránky s vloženým CSS stylem
    pass

@app.route('/plain')
def plain():
    # Vrácení čistého textu s nastaveným content-type
    pass

@app.route('/headers')
def headers():
    # Vrácení odpovědi s vlastními hlavičkami
    pass

@app.route('/xml')
def xml():
    # Vrácení XML odpovědi
    pass

@app.route('/csv')
def csv():
    # Vrácení CSV dat
    pass

@app.route('/set-cookie')
def set_cookie():
    # Nastavení cookie v odpovědi
    pass

@app.route('/get-cookie')
def get_cookie():
    # Získání hodnoty cookie z požadavku
    pass

@app.route('/status')
def status():
    # Vrácení pouze status kódu bez obsahu (např. 204)
    pass

@app.route('/json-list')
def json_list():
    # Vrácení JSON pole (seznam slovníků)
    pass

@app.route('/json-nested')
def json_nested():
    # Vrácení vnořeného JSON (slovník v slovníku)
    pass

@app.route('/html-table')
def html_table():
    # Vrácení HTML stránky s tabulkou
    pass

@app.route('/inline-js')
def inline_js():
    # Vrácení HTML stránky s JavaScriptem
    pass

@app.route('/inline-img')
def inline_img():
    # Vrácení HTML stránky s obrázkem
    pass

@app.route('/params')
def params():
    # Vrácení GET parametrů z URL
    pass

@app.route('/post-json', methods=['POST'])
def post_json():
    # Přijetí a vrácení JSON dat v POST požadavku
    pass

@app.route('/uppercase/<text>')
def uppercase(text):
    # Vrácení textu převedeného na velká písmena
    pass

@app.route('/repeat/<int:n>/<word>')
def repeat(n, word):
    # Vrácení slova opakovaného n-krát
    pass

if __name__ == '__main__':
    app.run(debug=True)