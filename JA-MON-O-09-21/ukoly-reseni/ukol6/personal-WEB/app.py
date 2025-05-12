from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        zprava = request.form.get('zprava')
        # Zde by se normálně zpracovala zpráva (např. odeslání e-mailem)
        message = "Děkujeme za zprávu, ozveme se vám!"
    return render_template('contact.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)