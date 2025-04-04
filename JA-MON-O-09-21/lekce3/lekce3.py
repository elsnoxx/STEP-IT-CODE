# Pracovní list: Tuples, Sets, Dictionaries, Search a Sort
import random
# ------------------------------------------------------------------------------
# 1. Tuples

# Úkol 1
# Vytvoř tuple, který obsahuje tři jména. Jak přistoupíš k druhému jménu?
tuplne_name = ("Alice", "Bob", "Adam")
print(tuplne_name[0])




# Úkol 2
# Vytvoř tuple obsahující názvy tří měst. Jak zjistíš, zda město "Praha" je v tomto tuple?
cities = ("Brno", "Ostrava", "Jihlava")

if "Praha" in cities:
    print("Je")
else:
    print("neni")



# Úkol 3: Rozbalení tuple
# Máš tuple obsahující tři hodnoty: ("Alice", 25, "Praha"). Jak rozbalíš tento tuple do tří proměnných?
person = ("Alice", 25, "Praha")

name = person[0]
age = person[1]
town = person[2]

print(f"{name} ma {age} let a bydli v {town}")

# ("Alice", 25 , "Praha")
# ( name  , age, town   )
name, age, town = person
print(f"{name} ma {age} let a bydli v {town}")


# Úkol 4: Výměna hodnot pomocí tuple
# Máš dvě proměnné a = 5 a b = 10. Jak prohodíš jejich hodnoty bez použití třetí proměnné?
a = 5
b = 10
print(f"Start: a = {a}, b = {b}")
# tmp = a
# a = b
# b = tmp
a, b = b, a
print(f"Swap: a = {a}, b = {b}")


# Úkol 5: Iterace přes tuple
# Máš tuple obsahující názvy měst: ("Brno", "Praha", "Ostrava"). Jak vypíšeš každé město na nový řádek?
cities = ("Brno", "Praha", "Ostrava")
for city in cities:
    print(city)

# Úkol 6: Zanořené tuple
# Máš tuple obsahující informace o osobách: (("Alice", 25), ("Bob", 30), ("Charlie", 22)).
# Jak získáš věk osoby jménem "Bob"?
people = (("Alice", 25), ("Bob", 30), ("Charlie", 22))

# print(people[1][1])
for person in people:
    if person[0] == "Bob":
        print(person[1])

# Hra: Uhádni hlavní město.
# Hráč hádá hlavní město podle zadaného státu. Pokud uhodne správně, vyhraje.
# Pokud ne, ukáže se správné hlavní město.
# Hráč má 5 pokusů. Po každém pokusu se zobrazí, kolik bodů získal.
# Hráč zadává stát a program porovná s hlavním městem.
# Hráč zadává svůj tip a program porovná s hlavním městem.
# Pokud uhodne správně, získá bod. Pokud ne, ukáže se správné hlavní město.

# Tuple obsahující dvojice (stát, hlavní město)
staty_a_mesta = (
    ("Česká republika", "Praha"),
    ("Slovensko", "Bratislava"),
    ("Německo", "Berlín"),
    ("Francie", "Paříž"),
    ("Španělsko", "Madrid"),
    ("Itálie", "Řím"),
    ("USA", "Washington"),
    ("Kanada", "Ottawa"),
    ("Japonsko", "Tokio"),
    ("Austrálie", "Canberra"),
    ("Rusko", "Moskva"),
    ("Čína", "Peking"),
    ("Indie", "Nové Dillí"),
    ("Brazílie", "Brasília"),
    ("Mexiko", "Mexiko"),
    ("Argentina", "Buenos Aires"),
    ("Jihoafrická republika", "Pretoria"),
    ("Egypt", "Káhira"),
    ("Turecko", "Ankara"),
    ("Řecko", "Atény"),
    ("Švédsko", "Stockholm"),
    ("Norsko", "Oslo"),
    ("Finsko", "Helsinky"),
    ("Dánsko", "Kodaň"),
    ("Polsko", "Varšava"),
    ("Rakousko", "Vídeň"),
    ("Maďarsko", "Budapešť"),
    ("Švýcarsko", "Bern"),
    ("Portugalsko", "Lisabon"),
    ("Nizozemsko", "Amsterdam"),
    ("Belgie", "Brusel"),
    ("Ukrajina", "Kyjev"),
    ("Vietnam", "Hanoj"),
    ("Thajsko", "Bangkok"),
    ("Indonésie", "Jakarta"),
    ("Nový Zéland", "Wellington"),
    ("Saúdská Arábie", "Rijád"),
    ("Izrael", "Jeruzalém"),
    ("Jižní Korea", "Soul"),
    ("Severní Korea", "Pchjongjang")
)


print("Vitejte ve hre kde vam pocitac zada stat a vy vypisete jeho hlavni mesto.")

pocet_kol = 5
body = 0

for kolo in range(pocet_kol):
    stat, hlavni_mesto = random.choice(staty_a_mesta)
    # print(f"Bot vybral {stat} a jeho hlavni mesto je {hlavni_mesto}")
    gues = input(f"Jake je hlavni mesto {stat}: ")

    if gues.lower() == hlavni_mesto.lower():
        print("Spravne uhadl jsi to a ziskavas bod")
        body += 1
    else:
        print("spatne neziskavas nic")

print(f"Konec hry uhadl jsi {body}/{pocet_kol}")

# ------------------------------------------------------------------------------
# 2. Sets

# Úkol 1
# Vytvoř set s několika čísly. Jak ověříš, zda číslo 5 je v tomto setu?
number_sets = {1, 2, 3, 4, 5, 6}
if 9 in number_sets:
    print("JE")
else:
    print("neni")



# Úkol 2
# Vytvoř set obsahující názvy zvířat. Přidej do tohoto setu nové zvíře "kočka".
animal_set = {"pes", "slon", "had"}
print(animal_set)
animal_set.add("kocka")
print(animal_set)

# Úkol 3: Operace na setech
# Máš dva sety: {1, 2, 3, 4} a {3, 4, 5, 6}. Jak zjistíš jejich průnik (společné prvky)?
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 & set2)



# Úkol 4: Odstranění prvku ze setu
# Máš set {1, 2, 3, 4, 5}. Jak odstraníš číslo 3?
numbers = {1, 2, 3, 4, 5}
print(numbers)
numbers.remove(3)
print(numbers)

# Úkol 5: Převod seznamu na set
# Máš seznam [1, 2, 2, 3, 4, 4, 5]. Jak vytvoříš set, který obsahuje pouze unikátní hodnoty?
numbers_list = [6, 6, 1, 2, 2, 3, 4, 4, 5]
print(numbers_list)
new_set = set(numbers_list)
print(new_set)



# Úkol 6: Spojení dvou setů
# Máš dva sety: {1, 2, 3} a {4, 5, 6}. Jak vytvoříš nový set, který obsahuje všechny prvky z obou setů?
set_a = {1, 2, 3}
set_b = {4, 5, 6}
print(set_a | set_b)

# & -> and, prunik
# if 1 == 1 and 2 == 2 -> pravda
# if 1 == 1 and 3 == 2 -> nepravda

# | -> or, spojeni
# if 1 == 1 or 2 == 3 -> pravda
# if 1 == 2 or 2 == 2 -> pravda
# if 1 == 2 or 3 == 2 -> nepravda

# Úkol 7: Generování setu z řetězce
# Máš řetězec "abrakadabra". Jak vytvoříš set obsahující unikátní znaky z tohoto řetězce?
string = "abrakadabra"
print(string)
new_char_set = set(string)
print(new_char_set)


# Úkol 8: Set z číselného rozsahu
# Jak vytvoříš set obsahující všechna sudá čísla od 1 do 10?
even_number = {}
even_number = set(even_number)
for i in range(1,11):
    if i % 2 == 0:
        even_number.add(i)
print(even_number)

# Hra: Najdi unikátní slova!
# Najdi unikátní slova ve větě a zjisti, kolik jich je.
# Hráč hádá počet unikátních slov ve větě.
# Pokud uhodne správně, vyhraje. Pokud ne, ukáže se správný počet.
# Hra je založena na náhodně vybrané větě z předem definovaného seznamu vět.
# Hráč zadá svůj tip a program porovná s počtem unikátních slov ve větě.
# Pokud uhodne správně, získá bod. Pokud ne, ukáže se správný počet unikátních slov.
import random
import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

vety = [
    "Python je skvělý a mocný programovací jazyk",
    "Hraní her v Pythonu je zábava",
    "Sety jsou užitečné pro odstranění duplicit",
    "Hledání unikátních slov je skvělý trénink",
    "Programování je dovednost, která se dá naučit",
    "Opakování je matka moudrosti",
    "Chyby jsou součástí učení, každý programátor je dělá",
    "Nejlepší způsob jak se naučit programovat je psát kód",
    "Python je interpretovaný jazyk s jednoduchou syntaxí",
    "Algoritmy a datové struktury jsou klíčem k efektivnímu kódu",
    "Verzování a kódu pomocí GitHubu je užitečné a pro spolupráci",
    "Každý programátor by měl znát alespoň jeden objektově orientovaný jazyk",
    "Čtení cizího kódu je stejně důležité jako jeho psaní",
    "Komentování kódu pomáhá ostatním i tobě v budoucnu",
    "Refaktoring kódu zlepšuje jeho čitelnost a efektivitu"
]

veta = random.choice(vety)
slova = veta.lower().replace(",", "").replace(".", "").split()
# print(veta)
# print(slova)

print(f"Veta zni: {veta}")
time.sleep(2)
clear_console()


while True:
    try:
        tip = int(input("Zadej pocet unikatnich slov: "))
        unikatni = set(slova)
        if tip == len(unikatni):
            print("Uhadl jsi")
            break
        elif tip > len(unikatni):
            print("Zkus to znova s mensim cislem")
        else:
            print("Zkus to znova ale zadej vetsi cislo")
        
    except ValueError:
        print("Prosim zadej cislo")
        



# ------------------------------------------------------------------------------
# 3. Dictionaries

# Úkol 1
# Vytvoř slovník, kde klíčem bude jméno a hodnotou věk. Jak získáš věk osoby jménem "Petr"?
people = {"Anna" : 18, "Bob" : 50, "Petr" : 45}
print(people.get("Petr"))

# Úkol 2
# Vytvoř set obsahující názvy zvířat. Přidej do tohoto setu nové zvíře "kočka".



# Úkol 3: Práce s hodnotami v dictionary
# Máš slovník {"jablko": 10, "banán": 5, "pomeranč": 8}. Jak zvýšíš počet jablek o 3?
fruits = {"jablko": 10, "banán": 5, "pomeranč": 8}
print(fruits)
fruits["jablko"] += 3
print(fruits)


# Úkol 4: Iterace přes dictionary
# Máš slovník {"Anna": 22, "Petr": 30, "Eva": 19}. Jak vypíšeš všechny klíče a hodnoty?
people_ages = {"Anna": 22, "Petr": 30, "Eva": 19}

for name, age in people_ages.items():
    print(f"{name} ma {age} let")



# Úkol 5: Získání hodnoty z dictionary s výchozí hodnotou
# Máš slovník {"auto": "BMW", "barva": "červená"}. Jak získáš hodnotu pro klíč "model", pokud neexistuje?
# car = {"auto": "BMW", "barva": "červená", "model": "M3"}
car = {"auto": "BMW", "barva": "červená"}
model = car.get("model", "neznami")
print(model)



# Úkol 6: Zanořené dictionaries
# Vytvoř slovník, kde klíčem bude jméno a hodnotou další slovník obsahující věk a město.
# Jak získáš město osoby jménem "Eva"?
nested_dict = {
    "Anna": {"věk": 22, "město": "Praha"},
    "Petr": {"věk": 30, "město": "Brno"},
    "Eva": {"věk": 19, "město": "Ostrava"}
}

print(nested_dict["Eva"]["město"])

# Hra: Duolingo
# Program vypíše náhodné české slovo a hráč musí napsat jeho anglický překlad.
# Pokud hráč odpoví správně, získá bod. Pokud ne, program mu ukáže správný překlad.
# Hráč může kdykoliv napsat "konec" a hra se ukončí.

prekladac = {
    "pes": "dog",
    "kočka": "cat",
    "dům": "house",
    "auto": "car",
    "škola": "school",
    "učitel": "teacher",
    "stůl": "table",
    "židle": "chair",
    "slunce": "sun",
    "měsíc": "moon",
    "voda": "water",
    "jídlo": "food",
    "přítel": "friend",
    "rodina": "family",
    "práce": "work",
    "kniha": "book",
    "telefon": "phone",
    "počítač": "computer",
    "okno": "window",
    "dveře": "door",
    "čas": "time",
    "den": "day",
    "noc": "night",
    "město": "city",
    "vesnice": "village",
    "cesta": "road",
    "letadlo": "plane",
    "vlak": "train",
    "loď": "ship",
    "ruka": "hand",
    "oko": "eye",
    "hlava": "head",
    "srdce": "heart",
    "moře": "sea",
    "hora": "mountain",
    "strom": "tree",
    "květina": "flower",
    "jablko": "apple",
    "banán": "banana",
    "chléb": "bread",
    "mléko": "milk",
    "sýr": "cheese",
    "cukr": "sugar",
    "sůl": "salt",
    "vítr": "wind",
    "déšť": "rain",
    "sníh": "snow",
    "led": "ice",
    "oheň": "fire",
    "země": "earth",
    "vzduch": "air"
}


print("Napis anglicky preklad vypsaneho slova.")
print("Pokud chces skoncit napis X")
print(prekladac.keys())
print(list(prekladac.keys()))

while True:
    ceske_slovo = random.choice(list(prekladac.keys()))
    odpoved = input(f"Jak se prelozi slovo {ceske_slovo} do anglictiny: ")

    if odpoved == "X":
        break

    if odpoved == prekladac[ceske_slovo]:
        print("SPravna odpoved")
    else:
        print(f"Spatne spravna odpoved je {prekladac[ceske_slovo]}")
    


# ------------------------------------------------------------------------------ 
# 4. Hledání (Search)

# Úkol 1: Základní hledání
# V seznamu [3, 7, 2, 9, 4] najdi, zda obsahuje číslo 9. Jaký způsob použiješ?
numbers_list = [3, 7, 2, 9, 4]
if 9 in numbers_list:
    print("Je")
else:
    print("neni")

# Úkol 2: Najdi index čísla
# Jak zjistíš index čísla 9 v seznamu?

print(numbers_list.index(9))
print(numbers_list[numbers_list.index(9)])


# ------------------------------------------------------------------------------ 
# 7. Třídění (Sort)

# Úkol 1: Seřaď seznam čísel vzestupně
unsorted_numbers = [8, 3, 1, 5, 2]
print(unsorted_numbers)
unsorted_numbers.sort()
print(unsorted_numbers)

# Úkol 2: Seřaď seznam čísel sestupně
unsorted_numbers = [8, 3, 1, 5, 2]
print(unsorted_numbers)
sorted_list = sorted(unsorted_numbers, reverse=True)
print(sorted_list)
# setrizeni vzestupne
sorted_list = sorted(unsorted_numbers, reverse=True)
print(sorted_list)

# Úkol 3: Třídění seznamu řetězců podle délky
words = ["Python", "je", "skvělý", "jazyk"]
print(words)
words.sort(key=len)
print(words)
