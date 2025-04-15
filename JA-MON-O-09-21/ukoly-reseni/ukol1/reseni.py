# ==============================================================================================================
# Úkol 1: Sestavení čísla z jednotlivých číslic
# Uživatel zadá tři jednotlivé číslice. Vytvoř program, který z těchto číslic sestaví jedno číslo.
# Příklad:
# Zadá-li uživatel čísla 1, 5, 7, výsledkem bude číslo 157.
# ==============================================================================================================


# zisk cisel od uzivatele z konzole
number1 = input("Zadej prvni cislisci: ")
number2 = input("Zadej druhou cislisci: ")
number3 = input("Zadej treti cislisci: ")

# kontrola, zda je prvni cislo nula
if number1 != '0':
    # pokud ano mohu spojit vsechny tri cislice do jednoho cisla
    print(number1 + number2 + number3)
else:
    print("Prvni cislo nemuze byt nula")

# ==============================================================================================================
# Úkol 2: Součin číslic čtyřciferného čísla
# Uživatel zadá čtyřciferné číslo. Vypočítej součin jeho jednotlivých číslic.
# Příklad:
# Zadá-li uživatel číslo 1324, výpočet bude 1 * 3 * 2 * 4 = 24.
# ==============================================================================================================

try:
    # zisk ctyrciferneho cisla od uzivatele z konzole
    number = int(input("Zadej ctryciferne cislo: "))

    # kontrola, zda je cislo ctyrciferne
    if number < 1000 or number > 9999:
        # pokud ne, vyhodim chybu
        print("Cislo musi mit 4 cifry")
        raise ValueError("Cislo musi mit 4 cifry")
    # pokud ano, ziskam jednotlivou cifru
    else:
        # prevedu cislo na string, abych mohl ziskat jednotlivou cifru
        number = str(number)
        # ziskam jednotlivou cifru a vynasobim je mezi sebou
        result = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
        print("Soucin cisel je: ", result)

# pokud uzivatel nezadal cislo, vyhodim chybu
except ValueError:
    print("Zadali jste neplatne cislo")

# ==============================================================================================================
# Úkol 3: Převod metrů na jiné jednotky
# Uživatel zadá délku v metrech. Převeď tuto hodnotu na:

# centimetry
# decimetry
# milimetry
# míle
# Výsledky zobraz přehledně v konzoli.
# ==============================================================================================================

print("Zadej delku v metrech: ")
# zisk delky od uzivatele z konzole
length = float(input())

# prevedu delku na jednotlivou jednotku a vypisi ji na konzoli
print("Centimetry: ", length * 100)
print("Decimetry: ", length * 10)
print("Milimetry: ", length * 1000)
print("Mile: ", length * 0.000621371)


# ==============================================================================================================
# Úkol 4: Výpočet obsahu trojúhelníku
# Uživatel zadá délku základny a výšku trojúhelníku. Program spočítá a vypíše obsah trojúhelníku.
# Vzorec: obsah = (základna * výška) / 2
# ==============================================================================================================

print("Zadej delku zakladny: ")
# zisk delky zakladny od uzivatele z konzole
base = float(input())
print("Zadej delku vysky: ")
height = float(input())

# vypocitam obsah trojuhelniku a vypisi ho na konzoli
print("Obsah trojuhelniku je: ", (base * height) / 2)


# ==============================================================================================================
# Úkol 5: Obrácení čtyřciferného čísla
# Uživatel zadá čtyřciferné číslo. Vytvoř program, který číslo obrátí.
# Příklad:
# Zadá-li uživatel číslo 4512, výstup bude 2154
# ==============================================================================================================

print("Zadej ctyrciferne cislo: ")
# zisk ctyrciferneho cisla od uzivatele z konzole
number = input()
number_reverse = ""

# Cyklus pro obrácení čísla
for index in range(len(number)):
    # Přidání poslední číslice na začátek nového čísla a získání poslední číslice pomocí indexu
    # len(number) - 1 - index --->  zajišťuje, že začínáme od poslední číslice
    # a postupně se posouváme k první číslici
    number_reverse += number[len(number) - 1 - index]

print("Obracene cislo je: ", number_reverse)