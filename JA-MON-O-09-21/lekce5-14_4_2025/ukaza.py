import requests
import json

# 1. Definujeme URL API koncového bodu
url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/"

ico = input("Zadej ico hledaneho subjeku: ")

url = url + ico
# 2. Odešleme GET požadavek na server
print("Odesílám požadavek na API...")
response = requests.get(url)

# 3. Zkontrolujeme, zda byl požadavek úspěšný (stavový kód 200)
if response.status_code == 200:
    # 4. Převedeme JSON odpověď na slovník Pythonu
    data = response.json()
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    # 5. Vypíšeme základní informace o ekonomickém subjektu
    print("\nZÁKLADNÍ INFORMACE O SUBJEKTU:")
    print(f"Název: {data['obchodniJmeno']}")
    print(f"IČO: {data['ico']}")
    print(f"Právní forma: {data['pravniForma']}")
    print(f"Stat: {data['sidlo']['nazevStatu']}")
    print(f"Adresa: {data['sidlo']['textovaAdresa']}")
else:
    print(f"Chyba při komunikaci s API. Stavový kód: {response.status_code}")