from flask import Flask, jsonify, abort

app = Flask(__name__)

# Textová odpověď
@app.route("/text")
def text():
    return "Ahoj světe!"

# HTML odpověď
@app.route("/html")
def html():
    return """
    <html>
        <head><title>HTML stránka</title></head>
        <body>
            <h1>Nadpis stránky</h1>
            <p>Toto je jednoduchý odstavec v HTML.</p>
        </body>
    </html>
    """

# JSON odpověď
@app.route("/json")
def json_response():
    return jsonify(status="ok", message="Všechno funguje!")

# Dynamický endpoint
@app.route("/<jmeno>")
def vitani(jmeno):
    return f"Vítej, {jmeno}!"

# Chybová stránka
@app.route("/error")
def error():
    abort(404)

if __name__ == "__main__":
    app.run(debug=True)