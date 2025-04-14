import requests
import random
import time

def get_pokemon_info(pokemon_name):
    """
    Získá informace o zadaném Pokémonovi
    """
    # Převeď jméno na malá písmena pro správné API volání
    pokemon_name = pokemon_name.lower()
    
    # TODO: Odešli GET požadavek na API https://pokeapi.co/api/v2/pokemon/{pokemon_name}
    # Tip: Použij requests.get() a ulož výsledek do proměnné response
    
    # TODO: Zkontroluj, zda byl požadavek úspěšný (status_code 200)
    # Pokud ne, vrať zprávu "Pokémon nenalezen"
    
    # TODO: Získej data ve formátu JSON
    
    # TODO: Z odpovědi extrahuj následující informace:
    # - jméno (data["name"])
    # - výšku v dm (data["height"])
    # - váhu v hg (data["weight"])
    # - obrázek (data["sprites"]["front_default"])
    # - typy (data["types"] - projdi seznam a získej ["type"]["name"])
    # - schopnosti (data["abilities"] - projdi seznam a získej ["ability"]["name"])
    
    # TODO: Vrať slovník s extrahovanými informacemi

def display_pokemon(pokemon_data):
    """
    Zobrazí informace o Pokémonovi v konzoli
    """
    # TODO: Zobraz informace o Pokémonovi v pěkném formátu
    # Například:
    # =======================
    # PIKACHU
    # =======================
    # Výška: 4 dm
    # Váha: 60 hg
    # Typy: electric
    # Schopnosti: static, lightning-rod
    # Obrázek: https://raw.githubusercontent.com/...
    
    # Doplň svůj kód

def pokemon_quiz():
    """
    Vytvoří jednoduchý kvíz o náhodném Pokémonovi
    """
    # Seznam známých Pokémonů pro kvíz
    popular_pokemon = ["pikachu", "charizard", "bulbasaur", "squirtle", "eevee", 
                       "jigglypuff", "mewtwo", "snorlax", "gengar", "gyarados"]
    
    # TODO: Vyber náhodného Pokémona ze seznamu
    
    # TODO: Získej data o tomto Pokémonovi
    
    # TODO: Polož uživateli otázku o tomto Pokémonovi
    # Například: "Jaký typ má Pokémon PIKACHU?"
    
    # TODO: Zkontroluj odpověď a informuj uživatele, zda odpověděl správně

# Hlavní menu
def main():
    print("==== POKÉMON PRŮVODCE ====")
    print("Vítej v aplikaci, která ti ukáže informace o Pokémonech!")
    
    while True:
        print("\nCo chceš dělat?")
        print("1. Vyhledat Pokémona podle jména")
        print("2. Zobrazit náhodného Pokémona")
        print("3. Zahrát si Pokémon kvíz")
        print("4. Konec")
        
        choice = input("Tvoje volba (1-4): ")
        
        # TODO: Zpracuj volbu uživatele a zavolej příslušné funkce
        # Doplň svůj kód

        pokemon_list = ["pikachu", "charizard", "bulbasaur", "squirtle", "eevee", "jigglypuff",
                        "mewtwo", "snorlax", "gengar", "gyarados", "ditto", "mew", "onix",
                        "dragonite", "alakazam", "machamp", "golem", "zapdos", "articuno"]
        
        # Například pro volbu 1:
        if choice == "1":
            name = input("Zadej jméno Pokémona: ")
            pokemon_data = get_pokemon_info(name)
            if "error" in pokemon_data:
                print(pokemon_data["error"])
            else:
                display_pokemon(pokemon_data)

# Spuštění hlavního programu
if __name__ == "__main__":
    main()