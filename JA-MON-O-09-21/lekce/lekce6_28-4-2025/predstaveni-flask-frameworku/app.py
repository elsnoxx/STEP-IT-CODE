from flask import Flask, request, render_template, redirect, url_for, abort

app = Flask(__name__)

# 1. Základní routy (Routes)
@app.route('/')
def home():
    return 'Hlavní stránka'

@app.route('/about')
def about():
    return 'O nás'

# 2. Dynamické routy
@app.route('/user/<username>')
def show_user(username):
    # Dynamický segment v URL
    return f'Uživatel: {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Dynamický segment s typem int
    return f'Příspěvek číslo: {post_id}'

@app.route('/category/<category>')
def show_category(category):
    # Dynamický segment s typem string
    return f'Kategorie: {category}'

# 3. HTTP metody (GET, POST)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Zpracování přihlášení
        return 'Zpracování přihlášení'
    else:
        # Zobrazení přihlašovacího formuláře
        return 'Přihlašovací formulář'

# 4. Templates (Šablony)
@app.route('/hello/<name>')
def hello(name):
    # Vykreslení šablony hello.html s proměnnou name
    return render_template('hello.html', name=name)

# 5. Zpracování formulářů
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Zdravím, {name}!'
    return '''
        <form method="post">
            <input name="name">
            <button type="submit">Odeslat</button>
        </form>
    '''

# 6. Redirecty a chyby
@app.route('/redirect')
def redirect_example():
    # Přesměrování na jinou stránku
    return redirect(url_for('home'))

@app.route('/error')
def error_example():
    # Vyvolání chyby 404
    abort(404)

# Vlastní stránka pro chybu 404
@app.errorhandler(404)
def page_not_found(e):
    return "Stránka nebyla nalezena", 404

if __name__ == '__main__':
    app.run(debug=True)