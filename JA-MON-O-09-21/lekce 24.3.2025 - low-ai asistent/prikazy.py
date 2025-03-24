import random
import math
import time
import utils
from colorama import Fore

def sudost_lichost():
    """
    Funkce zkontroluje, zda je zadané číslo sudé nebo liché a vypíše odpovídající zprávu.

    Funkce také ošetřuje neplatné vstupy, tedy pokud uživatel nezadá celé číslo.

    """
    while True:
        try:
            cislo = int(input("Zadej cislo: "))
            if cislo == 0:
                print(Fore.GREEN + "Nula neni ani suda ani licha")
            elif cislo % 2 == 0:
                print(Fore.GREEN + "Cislo je sude")
            else:
                print(Fore.GREEN + "Zadne cislo je liche")
            break
        except ValueError:
            print(Fore.RED + "Mas zadat cislo a ne nic jineho")

def nasobek_sedmi():
    """
    Funkce zjistí, zda je zadané číslo násobkem 7 a vypíše odpovídající zprávu.

    Pokud uživatel zadá neplatné číslo, bude požádán o nový vstup.

    """
    while True:
        try:
            cislo = int(input("Zadej cislo: "))
            if cislo % 7 == 0:
                print(Fore.GREEN + f"Zadane cislo {cislo} je nasobkem 7")
            else:
                print(Fore.RED + f"Zadane cislo {cislo} neni nasobkem 7")
        except ValueError:
            print(Fore.RED + "Mas zadat cislo a ne nic jineho")
  


def max_dvou_cisel():
    """
    Funkce zjistí, které zadané číslo (první nebo druhé) je větší, a vypíše výsledek.

    Funkce ošetřuje neplatné vstupy a požádá o nové číslo v případě chyby.

    :vstup a: První číslo
    :vstup b: Druhé číslo
    """
    while True:
        try:
            cislo1 = int(input("zadej prvni cislo: "))
            cislo2 = int(input("zadej druhe cislo: "))
            # if cislo1 > cislo2:
            #     print(Fore.GREEN + f"Cislo prvni tedy {cislo1} je vetsi nez {cislo2}")
            # elif cislo1 < cislo2:
            #     print(Fore.GREEN + f"Cislo prvni tedy {cislo2} je vetsi nez {cislo1}")
            # elif cislo1 == cislo2:
            #     print(Fore.GREEN + f"Cisla jsou stejna")
            print(Fore.GREEN + f"Nejvetsi cislo z cisel je {max(cislo1, cislo2)}")
            break
        except ValueError:
            print(Fore.RED + "spatny vstup")


def min_dvou_cisel():
    """
    Funkce zjistí, které zadané číslo (první nebo druhé) je menší, a vypíše výsledek.

    Funkce ošetřuje neplatné vstupy a požádá o nové číslo v případě chyby.

    :vstup a: První číslo
    :vstup b: Druhé číslo
    """
    while True:
        try:
            cislo1 = int(input("zadej prvni cislo: "))
            cislo2 = int(input("zadej druhe cislo: "))
            print(Fore.GREEN + f"Nejvetsi cislo z cisel je {min(cislo1, cislo2)}")
            break
        except ValueError:
            print(Fore.RED + "spatny vstup")



def aritmeticke_operace():
    """
    Funkce provádí základní aritmetické operace mezi dvěma zadanými čísly.

    Uživatel zadá dvě čísla a operaci (+, -, *, /). Funkce provede příslušnou operaci a vypíše výsledek.
    Pokud je zadaná neplatná operace nebo dojde k dělení nulou, funkce vypíše chybovou zprávu.

    :vstup a: První číslo pro operaci
    :vstup b: Druhé číslo pro operaci
    :vstup operace: Operace, kterou uživatel chce provést (+, -, *, /)
    """
    while True:
        try:
            a = int(input("Zadej prvni cislo: "))
            b = int(input("Zadej druhe cislo: "))
            operace = input("Vyber z operaci (+, -, *, /): ")

            if operace == "+":
                print(f"Zadal jsi cislo {a} a {b} a jejich soucet je {a + b}")
            elif operace == "-":
                print(f"Zadal jsi cislo {a} a {b} a jejich rozdil je {a - b}")
            elif operace == "*":
                print(f"Zadal jsi cislo {a} a {b} a jejich soucin je {a + b}")
            elif operace == "/":
                if b != 0:
                    print(f"Zadal jsi cislo {a} a {b} a jejich soucet je {a / b}")
                else:
                    print("nemohu delit nulou")

            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")


def prevod_sekund():
    """
    Funkce převádí zadaný čas v sekundách na hodiny, minuty a sekundy.

    Uživatel zadá čas v sekundách, a funkce vypíše odpovídající čas v hodinách, minutách a sekundách.

    :vstup sekundy: Čas v sekundách, který bude převeden na hodiny, minuty a sekundy.
    """


def obvod_obsah_kruhu():
    """
    Funkce vypočítá obvod nebo obsah kruhu na základě zadaného průměru.

    Uživatel si zvolí, zda chce vypočítat obvod nebo obsah kruhu, a funkce provede výpočet na základě zadaného průměru.

    :vstup prumer: Průměr kruhu, na základě kterého se vypočítá obvod nebo obsah.
    :vstup volba: Volba uživatele (o pro obvod, p pro obsah).
    """
    while True:
        try:
            prumer = float(input("zadej prumer kruhu: "))
            volba = input("Zvolte výpočet (o = obvod, p = obsah): ")

            if volba == "o":
                print(Fore.GREEN + f"Obvod kruhu je {math.pi * prumer}")
            elif volba == "p":
                print(Fore.GREEN + f"Obvod kruhu je {math.pi * (prumer / 2) ** 2}")
            else:
                print("Zadal jsi spatnou volbu")
                raise ValueError
            break
        except ValueError:
            print("Chyba zadej znova")


def generuj_nahodne_cislo():
    """
    Funkce vygeneruje náhodné číslo mezi 1 a 100 a vypíše ho.

    :vstup None: Funkce nevyžaduje žádné parametry.
    """
    cislo_random = random.randint(1, 100)
    print(f"Vygenerovane random cislo je {cislo_random}")


def vypocet_ceny():
    """
    Funkce vypočítá cenu objednávky na základě zadaného množství, ceny za jednotku a slevy.

    Uživatel zadá množství, cenu za jednotku a slevu v procentech, funkce vypočítá celkovou cenu objednávky.

    :vstup mnozstvi: Množství zboží, které si uživatel objednává.
    :vstup cena: Cena za jednu jednotku zboží.
    :vstup sleva: Slevová procenta, která budou odečtena od celkové ceny.
    """


def doba_stahovani():
    """
    Funkce vypočítá dobu stahování souboru na základě zadané velikosti souboru a rychlosti stahování.

    Uživatel zadá velikost souboru v MB a rychlost stahování v Mbps, funkce vypočítá dobu stahování v minutách.

    :vstup velikost: Velikost souboru v MB.
    :vstup rychlost: Rychlost stahování v Mbps.
    """

def casove_pozdravy():
    """
    Funkce vypíše pozdrav na základě zadané hodiny.

    Uživatel zadá hodinu (0-23), a funkce vypíše odpovídající pozdrav:
    - Ráno (0-5)
    - Den (6-11)
    - Odpoledne (12-17)
    - Večer (18-23)
    
    :vstup hodina: Číslo hodiny, podle kterého se určí pozdrav.
    """



def stastne_cislo():
    """
    Funkce zjistí, zda je zadané číslo šťastné.

    Uživatel zadá šestimístné číslo. Funkce zjistí, zda se číslo transformuje na 1 (šťastné číslo)
    nebo zda se dostane do cyklu vedoucího k číslu 4 (nešťastné číslo).

    :vstup cislo: Šestimístné číslo, které je kontrolováno na štěstí.
    """



def prohozeni_cislic():
    """
    Funkce prohodí první a poslední číslici zadaného šestimístného čísla.

    Uživatel zadá šestimístné číslo a funkce prohodí první a poslední číslici a zobrazí výsledek.

    :vstup cislo: Šestimístné číslo, jehož první a poslední číslici budeme prohazovat.
    """


def rocni_obdobi():
    """
    Funkce vypíše roční období na základě zadaného čísla měsíce.

    Uživatel zadá číslo měsíce (1-12), a funkce určí roční období:
    - Zima (12, 1, 2)
    - Jaro (3, 4, 5)
    - Léto (6, 7, 8)
    - Podzim (9, 10, 11)

    :vstup mesic: Číslo měsíce, podle kterého se určí roční období.
    """


def vypis_vsech_cisel():
    """
    Funkce vypíše všechna čísla v zadaném rozsahu.

    Uživatel zadá počáteční a koncové číslo a funkce vypíše všechny čísla v tomto rozsahu (včetně).
    
    :vstup zacatek: Počáteční číslo rozsahu.
    :vstup konec: Konec čísla rozsahu.
    """


def vypis_lichych_cisel():
    """
    Funkce vypíše všechna lichá čísla v zadaném rozsahu.

    Uživatel zadá počáteční a koncové číslo a funkce vypíše pouze lichá čísla v tomto rozsahu.
    
    :vstup zacatek: Počáteční číslo rozsahu.
    :vstup konec: Konec čísla rozsahu.
    """


def vypis_cisel_sestupne():
    """
    Funkce vypíše čísla v sestupném pořadí.

    Uživatel zadá počáteční a koncové číslo, a funkce vypíše čísla v sestupném pořadí mezi těmito dvěma čísly.
    
    :vstup zacatek: Počáteční číslo pro sestupné řazení.
    :vstup konec: Konec čísla pro sestupné řazení.
    """


def vypis_sudych_cisel():
    """
    Funkce vypíše všechna sudá čísla v zadaném rozsahu.

    Uživatel zadá počáteční a koncové číslo a funkce vypíše pouze sudá čísla v tomto rozsahu.
    
    :vstup zacatek: Počáteční číslo rozsahu.
    :vstup konec: Konec čísla rozsahu.
    """


def serazeni_rozsahu():
    """
    Funkce seřadí čísla v zadaném rozsahu vzestupně.

    Uživatel zadá počáteční a koncové číslo a funkce seřadí čísla v tomto rozsahu vzestupně a vypíše je.
    
    :vstup zacatek: Počáteční číslo rozsahu.
    :vstup konec: Konec čísla rozsahu.
    """


def vypis_korekce_poradi():
    """
    Funkce seřadí čísla v zadaném rozsahu a vypíše je v seřazeném pořadí.

    Uživatel zadá počáteční a koncové číslo a funkce seřadí čísla v tomto rozsahu a vypíše je.
    
    :vstup zacatek: Počáteční číslo rozsahu.
    :vstup konec: Konec čísla rozsahu.
    """


def tabulka_nasobeni():
    """
    Funkce vypíše násobilku pro zadané číslo.

    Uživatel zadá číslo, pro které bude vypočítána násobilka (1-10).
    
    :vstup cislo: Číslo, pro které se vypíše násobilka.
    """


def prevod_men():
    """
    Funkce provádí převod mezi měnami.

    Uživatel zadá částku a měnu, kterou chce převést, a cílovou měnu. Funkce vypočítá a vypíše 
    odpovídající částku v cílové měně na základě přednastavených kurzů.

    :vstup cislo: Částka, kterou chcete převést.
    :vstup z_mena: Měna, kterou chcete převést (CZK, EUR, USD).
    :vstup na_mena: Měna, na kterou chcete převést (CZK, EUR, USD).
    """
    menove_kurzy = {
        "CZK": 1,
        "EUR": 24.5,
        "USD": 22.0
    }


def hraj_hadej_cislo():
    """
    Funkce implementuje hru "Hádej číslo", kde hráč hádá náhodně vybrané číslo mezi 1 a 100.

    Hráč se pokouší uhodnout číslo. Po každém pokusu mu bude sděleno, zda je zadané číslo
    příliš malé, příliš velké, nebo správné. Hra končí, když hráč uhodne číslo.
    
    :vstup cislo_k_hadani: Náhodně vybrané číslo, které hráč hádá.
    :vstup pokusy: Počet pokusů, které hráč udělal.
    """

def mark_number_in_list():
    """
    Funkce označí zadané číslo v seznamu čísel.

    Uživatel zadá seznam čísel a číslo, které chce označit. Všechna čísla jsou vypsána
    a číslo, které uživatel zadal, je zvýrazněno vykřičníkem.
    
    :vstup numbers: Seznam čísel, ve kterém se hledá číslo k označení.
    :vstup target: Číslo, které má být označeno v seznamu.
    """


def table_of_multiplication():
    """
    Funkce vypíše násobilku pro zadané číslo.

    Uživatel zadá číslo a funkce vypíše jeho násobilku (1 až 10).
    
    :vstup number: Číslo, pro které bude vypočítána násobilka.
    """



def zpracuj_prikaz(volba):
    """
    Funkce zpracovává uživatelskou volbu a volá odpovídající funkci podle čísla volby.

    Uživatel zadá číslo volby, které odpovídá konkrétní funkci. Funkce následně
    zavolá příslušnou funkci podle zadání. Pokud je volba neplatná, vypíše chybu.

    :param volba: Číslo volby, kterou uživatel zadal.
    """
    prikazy = {
        "1": sudost_lichost,
        "2": nasobek_sedmi,
        "3": max_dvou_cisel,
        "4": min_dvou_cisel,
        "5": aritmeticke_operace,
        "6": prevod_sekund,
        "7": obvod_obsah_kruhu,
        "8": generuj_nahodne_cislo,
        "9": vypocet_ceny,
        "10": doba_stahovani,
        "11": casove_pozdravy,
        "12": stastne_cislo,
        "13": prohozeni_cislic,
        "14": rocni_obdobi,
        "15": vypis_vsech_cisel,
        "16": vypis_lichych_cisel,
        "17": vypis_cisel_sestupne,
        "18": vypis_sudych_cisel,
        "19": serazeni_rozsahu,
        "20": vypis_korekce_poradi,
        "21": prevod_men,
        "22": generuj_nahodne_cislo,
        "23": hraj_hadej_cislo,
        "24": utils.read_from_file,
        "25": exit
    }

    if volba in prikazy:
        prikazy[volba]()
    else:
        print(Fore.RED + "Neplatná volba, zkuste to znovu.")