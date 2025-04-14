import requests

# URL API a klíč
url = 'https://api.weatherapi.com/v1/current.json'
params = {
    'key': '939716ed2d204c008ef151039252603',
    'q': 'Prague'
}

# Odeslání GET požadavku
response = requests.get(url, params=params)

# Získání dat ve formátu JSON
data = response.json()

# Výpis informací o počasí
print(f"Město: {data['location']['name']}")
print(f"Teplota: {data['current']['temp_c']} °C")
print(f"Stav: {data['current']['condition']['text']}")