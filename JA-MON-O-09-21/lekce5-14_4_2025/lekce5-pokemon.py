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
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    # print(url)
    response = requests.get(url)
    
    # TODO: Zkontroluj, zda byl požadavek úspěšný (status_code 200)
    # Pokud ne, vrať zprávu "Pokémon nenalezen"
    if response.status_code != 200:
        return {"error" : "Pokémon nenalezen"}
    
    # TODO: Získej data ve formátu JSON
    data = response.json()
    # print(data)
    
    # TODO: Z odpovědi extrahuj následující informace:
    # - jméno (data["name"])
    # - výšku v dm (data["height"])
    # - váhu v hg (data["weight"])
    # - obrázek (data["sprites"]["front_default"])
    # - typy (data["types"] - projdi seznam a získej ["type"]["name"])
    # - schopnosti (data["abilities"] - projdi seznam a získej ["ability"]["name"])
    # info = {
    #     "name" : data["name"],
    #     "height" : data["height"],
    #     "weight" : data["weight"],
    #     "image" : data["sprites"]["front_default"],
    #     "types": [type_info["type"]["name"] for type_info in data["types"]],
    #     "abilities": [ability_info["ability"]["name"] for ability_info in data["abilities"]]
    # }

    info = {
        "name" : data["name"],
        "height" : data["height"],
        "weight" : data["weight"],
        "image" : data["sprites"]["front_default"]
    }

    abilities = data["abilities"]
    abilities_list = []
    for abilitie in abilities:
        abilities_list.append(abilitie["ability"]["name"])
    
    info["abilities"] = abilities_list

    abilities = data["types"]
    types_list = []
    for abilitie in abilities:
        types_list.append(abilitie["type"]["name"])
    
    info["types"] = types_list
    # print(info)

    # TODO: Vrať slovník s extrahovanými informacemi
    return info
    

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
    print("=" * 22)
    print(pokemon_data["name"])
    print("=" * 22)
    print(f"Výška: {pokemon_data["height"]} dm")
    print(f"Váha: {pokemon_data["weight"]} hg")
    print(f"Typy: {', '.join(pokemon_data["types"])}")
    print(f"Schopnosti: {', '.join(pokemon_data["abilities"])}")
    print(f"Obrázek: {pokemon_data["image"]}")

def pokemon_quiz():
    """
    Vytvoří jednoduchý kvíz o náhodném Pokémonovi
    """
    # Seznam známých Pokémonů pro kvíz
    popular_pokemon = ["pikachu", "charizard", "bulbasaur", "squirtle", "eevee", 
                       "jigglypuff", "mewtwo", "snorlax", "gengar", "gyarados"]
    
    # TODO: Vyber náhodného Pokémona ze seznamu
    random_pokemon = random.choice(popular_pokemon)

    # TODO: Získej data o tomto Pokémonovi
    info = get_pokemon_info(random_pokemon)
    if "error" in info:
        print("Nastala chyba")
        return
    
    # TODO: Polož uživateli otázku o tomto Pokémonovi
    # Například: "Jaký typ má Pokémon PIKACHU?"
    print(f"Jaký typ má Pokémon {info["name"]}")
    

    
    # TODO: Zkontroluj odpověď a informuj uživatele, zda odpověděl správně
    count = 0
    guests = []
    while True:
        answer = input("Zadej typ pokemona: ")
        if answer in info["types"]:
            if answer not in guests:
                print("Spravne uhadl jsi")
                guests.append(answer)
                count += 1
            else:
                print("jiz uhadnute")
        else:
            print("spatne")
        
        if count == len(info["types"]):
            print("uhadl jsi vse")
            break

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
                # {"error": "Pokemon nenalezen"}
                print(pokemon_data["error"])
            else:
                display_pokemon(pokemon_data)
        if choice == "2":
            random_pokemon = random.choice(pokemon_list)
            pokemon_data = get_pokemon_info(random_pokemon)
            display_pokemon(pokemon_data)
        if choice == "3":
            pokemon_quiz()
        if choice == "4":
            print("Program se ukoncuje")
            break
        if choice not in ["1", "2", "3", "4"]:
            print("neplatna volba zkus to znova")

# Spuštění hlavního programu
if __name__ == "__main__":
    main()