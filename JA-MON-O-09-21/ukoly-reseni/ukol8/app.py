from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    # Získání aktuální polohy ISS
    iss_url = "http://api.open-notify.org/iss-now.json"
    iss_data = {}
    try:
        resp = requests.get(iss_url)
        resp.raise_for_status()
        data = resp.json()
        if data["message"] == "success":
            dt = datetime.fromtimestamp(data["timestamp"])
            iss_data = {
                "time": dt.strftime('%d.%m.%Y %H:%M:%S'),
                "latitude": data["iss_position"]["latitude"],
                "longitude": data["iss_position"]["longitude"]
            }
    except Exception as e:
        iss_data = {"error": str(e)}

    # Získání lidí ve vesmíru
    people_url = "http://api.open-notify.org/astros.json"
    people = []
    try:
        resp = requests.get(people_url)
        resp.raise_for_status()
        data = resp.json()
        if data["message"] == "success":
            people = data["people"]
    except Exception as e:
        people = [{"name": "Chyba při načítání", "craft": str(e)}]

    return render_template("index.html", iss=iss_data, people=people)

if __name__ == "__main__":
    app.run(debug=True)