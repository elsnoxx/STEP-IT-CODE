from flask import Flask, request, render_template, redirect, url_for, abort

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

# cesta k filmu Batman
@app.route("/batman")
def batman():
    return render_template("batman.html")

# cesta k filmu Inception
@app.route("/inception")
def inception():
    return render_template("inception.html")

# cesta k filmu avengers
@app.route("/avengers")
def avengers():
    return render_template("avengers.html")

# cesta k filmu minecraft
@app.route("/minecraft")
def minecraft():
    return render_template("minecraft.html")

# cesta k filmu gta5
@app.route("/gta5")
def gta5():
    return render_template("gta5.html")

# cesta k filmu callofduty
@app.route("/callofduty")
def callofduty():
    return render_template("callofduty.html")



if __name__ == '__main__':
    app.run(debug=True)