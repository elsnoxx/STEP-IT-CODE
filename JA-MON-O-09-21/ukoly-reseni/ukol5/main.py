import requests  # Import knihovny requests pro práci s HTTP požadavky (stahování dat z internetu)
from datetime import datetime  # Import třídy datetime pro převod časového razítka na čitelný formát

def get_iss_position():
    """
    Funkce stáhne a vypíše aktuální polohu Mezinárodní vesmírné stanice (ISS).
    """
    url = "http://api.open-notify.org/iss-now.json"  # URL API pro aktuální polohu ISS
    try:
        response = requests.get(url)  # Odeslání GET požadavku na API
        response.raise_for_status()   # Vyvolá výjimku, pokud odpověď obsahuje HTTP chybu
        data = response.json()        # Převede odpověď z JSON formátu na slovník
        if data["message"] == "success":
            timestamp = data["timestamp"]  # Unixové časové razítko
            dt = datetime.fromtimestamp(timestamp)  # Převod časového razítka na objekt datetime
            latitude = data["iss_position"]["latitude"]    # Získání zeměpisné šířky ISS
            longitude = data["iss_position"]["longitude"]  # Získání zeměpisné délky ISS
            print(f"\nAktuální poloha ISS:")
            print(f"Čas: {dt.strftime('%d.%m.%Y %H:%M:%S')}")  # Vypsání času v čitelném formátu
            print(f"Zeměpisná šířka: {latitude}")              # Vypsání šířky
            print(f"Zeměpisná délka: {longitude}\n")           # Vypsání délky
        else:
            print("Chyba při získávání dat o ISS.")  # Pokud API nevrátí úspěch
    except Exception as e:
        print(f"Chyba: {e}")  # Zachytí a vypíše jakoukoliv chybu (např. síťová chyba)

def get_people_in_space():
    """
    Funkce stáhne a vypíše seznam lidí, kteří jsou aktuálně ve vesmíru.
    """
    url = "http://api.open-notify.org/astros.json"  # URL API pro seznam lidí ve vesmíru
    try:
        response = requests.get(url)  # Odeslání GET požadavku na API
        response.raise_for_status()   # Kontrola případné HTTP chyby
        data = response.json()        # Převede odpověď z JSON na slovník
        if data["message"] == "success":
            print(f"\nLidé aktuálně ve vesmíru ({data['number']}):")  # Vypsání počtu lidí
            for person in data["people"]:  # Pro každý záznam osoby ve vesmíru
                print(f"- {person['name']} ({person['craft']})")  # Vypsání jména a stanice/lodi
            print()
        else:
            print("Chyba při získávání seznamu osob ve vesmíru.")  # Pokud API nevrátí úspěch
    except Exception as e:
        print(f"Chyba: {e}")  # Zachytí a vypíše jakoukoliv chybu

def main():
    """
    Hlavní funkce programu – zobrazí menu a zpracovává volby uživatele.
    """
    while True:  # Nekonečný cyklus, dokud uživatel nezvolí konec
        print("Vyber možnost:")
        print("1. Zobrazit aktuální polohu ISS")
        print("2. Vypsat osoby ve vesmíru")
        print("3. Konec")
        choice = input("Zadej volbu (1-3): ").strip()  # Načtení volby uživatele
        if choice == "1":
            get_iss_position()  # Zavolá funkci pro zobrazení polohy ISS
        elif choice == "2":
            get_people_in_space()  # Zavolá funkci pro zobrazení lidí ve vesmíru
        elif choice == "3":
            print("Ukončuji program.")  # Ukončí program
            break
        else:
            print("Neplatná volba, zkus to znovu.\n")  # Ošetření neplatné volby

if __name__ == "__main__":
    main()  # Spuštění hlavní funkce při přímém spuštění souboru