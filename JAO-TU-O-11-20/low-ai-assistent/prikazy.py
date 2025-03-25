import random
import math
import utils
from colorama import Fore

def sudost_lichost():
    """
    Funkce zkontroluje, zda je zadané číslo sudé nebo liché a vypíše odpovídající zprávu.

    Funkce také ošetřuje neplatné vstupy, tedy pokud uživatel nezadá celé číslo.

    """
    while True:
        try:
            cislo = int(input("Zadejte číslo: "))
            if cislo == 0:
                print(Fore.RED + "Nula není ani sudá, ani lichá.")
                utils.log_to_file("Uživatel zadal číslo 0.")
            elif cislo % 2 == 0:
                print(Fore.GREEN + f"{cislo} je sudé.")
                utils.log_to_file(f"Uživatel zadal sudé číslo: {cislo}")
            else:
                print(Fore.RED + f"{cislo} je liché.")
                utils.log_to_file(f"Uživatel zadal liché číslo: {cislo}")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání čísla.")

def nasobek_sedmi():
    """
    Funkce zjistí, zda je zadané číslo násobkem 7 a vypíše odpovídající zprávu.

    Pokud uživatel zadá neplatné číslo, bude požádán o nový vstup.

    """
    while True:
        try:
            cislo = int(input("Zadejte číslo: "))
            if cislo % 7 == 0:
                print(Fore.GREEN + f"{cislo} je násobkem 7.")
                utils.log_to_file(f"Uživatel zadal číslo násobek 7: {cislo}")
            else:
                print(Fore.RED + f"{cislo} není násobkem 7.")
                utils.log_to_file(f"Uživatel zadal číslo nenásobek 7: {cislo}")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání čísla.")  


def max_dvou_cisel():
    """
    Funkce zjistí, které zadané číslo (první nebo druhé) je větší, a vypíše výsledek.

    Funkce ošetřuje neplatné vstupy a požádá o nové číslo v případě chyby.

    :vstup a: První číslo
    :vstup b: Druhé číslo
    """
    while True:
        try:
            a = int(input("Zadejte první číslo: "))
            b = int(input("Zadejte druhé číslo: "))
            print(Fore.CYAN + f"Maximum je: {max(a, b)}")
            utils.log_to_file(f"Uživatel zadal čísla {a} a {b}, maximum je {max(a, b)}")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání čísel.")

def min_dvou_cisel():
    """
    Funkce zjistí, které zadané číslo (první nebo druhé) je menší, a vypíše výsledek.

    Funkce ošetřuje neplatné vstupy a požádá o nové číslo v případě chyby.

    :vstup a: První číslo
    :vstup b: Druhé číslo
    """
    while True:
        try:
            a = int(input("Zadejte první číslo: "))
            b = int(input("Zadejte druhé číslo: "))
            print(Fore.CYAN + f"Minimum je: {min(a, b)}")
            utils.log_to_file(f"Uživatel zadal čísla {a} a {b}, minimum je {min(a, b)}")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání čísel.")


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
            a = int(input("Zadejte první číslo: "))
            b = int(input("Zadejte druhé číslo: "))
            operace = input("Vyberte operaci (+, -, *, /): ")

            if operace == "+":
                print(Fore.CYAN + f"Výsledek: {a + b}")
                utils.log_to_file(f"Uživatel zadal čísla {a} a {b}, operace +, výsledek {a + b}")
            elif operace == "-":
                print(Fore.CYAN + f"Výsledek: {a - b}")
                utils.log_to_file(f"Uživatel zadal čísla {a} a {b}, operace -, výsledek {a - b}")
            elif operace == "*":
                print(Fore.CYAN + f"Výsledek: {a * b}")
                utils.log_to_file(f"Uživatel zadal čísla {a} a {b}, operace *, výsledek {a * b}")
            elif operace == "/":
                if b != 0:
                    print(Fore.CYAN + f"Výsledek: {a / b}")
                    utils.log_to_file(f"Uživatel zadal čísla {a} a {b}, operace /, výsledek {a / b}")
                else:
                    print(Fore.RED + "Dělení nulou není možné!")
                    utils.log_to_file("Uživatel se pokusil dělit nulou.")
            else:
                print(Fore.RED + "Neplatná operace.")
                utils.log_to_file(f"Uživatel zadal neplatnou operaci: {operace}")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání čísel nebo operace.")


def prevod_sekund():
    """
    Funkce převádí zadaný čas v sekundách na hodiny, minuty a sekundy.

    Uživatel zadá čas v sekundách, a funkce vypíše odpovídající čas v hodinách, minutách a sekundách.

    :vstup sekundy: Čas v sekundách, který bude převeden na hodiny, minuty a sekundy.
    """
    while True:
        try:
            sekundy = int(input("Zadejte čas v sekundách: "))
            hodiny = sekundy // 3600
            minuty = (sekundy % 3600) // 60
            sekundy = sekundy % 60
            print(Fore.YELLOW + f"Do půlnoci zbývá: {hodiny} hodin, {minuty} minut, {sekundy} sekund.")
            utils.log_to_file(f"Uživatel zadal čas v sekundách: {hodiny} hodin, {minuty} minut, {sekundy} sekund.")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání času v sekundách.")
def obvod_obsah_kruhu():
    """
    Funkce vypočítá obvod nebo obsah kruhu na základě zadaného průměru.

    Uživatel si zvolí, zda chce vypočítat obvod nebo obsah kruhu, a funkce provede výpočet na základě zadaného průměru.

    :vstup prumer: Průměr kruhu, na základě kterého se vypočítá obvod nebo obsah.
    :vstup volba: Volba uživatele (o pro obvod, p pro obsah).
    """
    while True:
        try:
            prumer = float(input("Zadejte průměr kruhu: "))
            volba = input("Zvolte výpočet (o = obvod, p = obsah): ")

            if volba == "o":
                print(f"Obvod kruhu: {math.pi * prumer}")
                utils.log_to_file(f"Uživatel zadal průměr {prumer}, výpočet obvodu.")
            elif volba == "p":
                print(f"Obsah kruhu: {math.pi * (prumer / 2) ** 2}")
                utils.log_to_file(f"Uživatel zadal průměr {prumer}, výpočet obsahu.")
            else:
                print(Fore.RED + "Neplatná volba.")
                utils.log_to_file(f"Uživatel zadal neplatnou volbu: {volba}")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím číslo.")
            utils.log_to_file("Neplatný vstup při zadávání průměru kruhu.")


def generuj_nahodne_cislo():
    """
    Funkce vygeneruje náhodné číslo mezi 1 a 100 a vypíše ho.

    :vstup None: Funkce nevyžaduje žádné parametry.
    """
    cislo = random.randint(1, 100)
    print(Fore.MAGENTA + f"Vygenerované číslo: {cislo}")
    utils.log_to_file(f"Vygenerované číslo: {cislo}")

def vypocet_ceny():
    """
    Funkce vypočítá cenu objednávky na základě zadaného množství, ceny za jednotku a slevy.

    Uživatel zadá množství, cenu za jednotku a slevu v procentech, funkce vypočítá celkovou cenu objednávky.

    :vstup mnozstvi: Množství zboží, které si uživatel objednává.
    :vstup cena: Cena za jednu jednotku zboží.
    :vstup sleva: Slevová procenta, která budou odečtena od celkové ceny.
    """
    while True:
        try:
            mnozstvi = int(input("Zadejte množství: "))
            cena = float(input("Zadejte cenu za jednotku: "))
            sleva = float(input("Zadejte slevu v procentech: "))
            celkova_cena = mnozstvi * cena * (1 - sleva / 100)
            print(f"Cena objednávky je: {celkova_cena} Kč")
            utils.log_to_file(f"Uživatel zadal množství {mnozstvi}, cenu za jednotku {cena}, slevu {sleva}%, celková cena {celkova_cena} Kč")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím platná čísla.")
            utils.log_to_file("Neplatný vstup při zadávání množství, ceny nebo slevy.")


def doba_stahovani():
    """
    Funkce vypočítá dobu stahování souboru na základě zadané velikosti souboru a rychlosti stahování.

    Uživatel zadá velikost souboru v MB a rychlost stahování v Mbps, funkce vypočítá dobu stahování v minutách.

    :vstup velikost: Velikost souboru v MB.
    :vstup rychlost: Rychlost stahování v Mbps.
    """
    while True:
        try:
            velikost = float(input("Zadejte velikost souboru v MB: "))
            rychlost = float(input("Zadejte rychlost stahování v Mbps: "))
            doba = velikost / (rychlost / 8)
            print(f"Doba stahování je: {doba} minut")
            utils.log_to_file(f"Uživatel zadal velikost souboru {velikost} MB, rychlost stahování {rychlost} Mbps, doba stahování {doba} minut")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím platná čísla.")
            utils.log_to_file("Neplatný vstup při zadávání velikosti souboru nebo rychlosti stahování.")


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
    while True:
        try:
            cislo = input("Zadejte číslo pro kontrolu (šestimístné): ")
            if len(cislo) != 6 or not cislo.isdigit():
                print(Fore.RED + "Neplatný vstup. Zadejte prosím šestimístné číslo.")
                utils.log_to_file("Neplatný vstup při zadávání šestimístného čísla.")
                continue

            cislo = int(cislo)
            navstevovane = set()
            
            while cislo != 1 and cislo != 4:
                if cislo in navstevovane:
                    print(Fore.RED + f"{cislo} není šťastné číslo.")
                    utils.log_to_file(f"Číslo {cislo} není šťastné číslo.")
                    break
                navstevovane.add(cislo)
                cislo = sum(int(digit)**2 for digit in str(cislo))
            if cislo == 1:
                print(Fore.GREEN + f"{cislo} je šťastné číslo.")
                utils.log_to_file(f"Číslo {cislo} je šťastné číslo.")
            elif cislo == 4:
                print(Fore.RED + f"{cislo} není šťastné číslo.")
                utils.log_to_file(f"Číslo {cislo} není šťastné číslo.")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání šestimístného čísla.")

def stastne_cislo():
    """
    Funkce zjistí, zda je zadané číslo šťastné.

    Uživatel zadá šestimístné číslo. Funkce zjistí, zda se číslo transformuje na 1 (šťastné číslo)
    nebo zda se dostane do cyklu vedoucího k číslu 4 (nešťastné číslo).

    :vstup cislo: Šestimístné číslo, které je kontrolováno na štěstí.
    """
    while True:
        try:
            cislo = input("Zadejte šestimístné číslo pro prohození číslic: ")
            if len(cislo) != 6 or not cislo.isdigit():
                print(Fore.RED + "Neplatný vstup. Zadejte prosím šestimístné číslo.")
                utils.log_to_file("Neplatný vstup při zadávání šestimístného čísla.")
                continue

            cislo = list(cislo)
            cislo[0], cislo[-1] = cislo[-1], cislo[0]
            prohozeno = ''.join(cislo)

            print(Fore.CYAN + f"Po prohození číslic je nové číslo: {prohozeno}")
            utils.log_to_file(f"Uživatel zadal číslo {cislo}, po prohození: {prohozeno}")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání šestimístného čísla.")


def prohozeni_cislic():
    """
    Funkce prohodí první a poslední číslici zadaného šestimístného čísla.

    Uživatel zadá šestimístné číslo a funkce prohodí první a poslední číslici a zobrazí výsledek.

    :vstup cislo: Šestimístné číslo, jehož první a poslední číslici budeme prohazovat.
    """
    while True:
        try:
            cislo = input("Zadejte šestimístné číslo pro prohození číslic: ")
            if len(cislo) != 6 or not cislo.isdigit():
                print(Fore.RED + "Neplatný vstup. Zadejte prosím šestimístné číslo.")
                utils.log_to_file("Neplatný vstup při zadávání šestimístného čísla.")
                continue

            cislo = list(cislo)
            cislo[0], cislo[-1] = cislo[-1], cislo[0]
            prohozeno = ''.join(cislo)

            print(Fore.CYAN + f"Po prohození číslic je nové číslo: {prohozeno}")
            utils.log_to_file(f"Uživatel zadal číslo {cislo}, po prohození: {prohozeno}")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání šestimístného čísla.")

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
    while True:
        try:
            mesic = int(input("Zadejte číslo měsíce (1-12): "))
            if mesic == 1 or mesic == 2 or mesic == 12:
                print(Fore.GREEN + "Zima")
                utils.log_to_file(f"Uživatel zadal měsíc {mesic}, roční období: Zima")
            elif mesic == 3 or mesic == 4 or mesic == 5:
                print(Fore.GREEN + "Jaro")
                utils.log_to_file(f"Uživatel zadal měsíc {mesic}, roční období: Jaro")
            elif mesic == 6 or mesic == 7 or mesic == 8:
                print(Fore.GREEN + "Léto")
                utils.log_to_file(f"Uživatel zadal měsíc {mesic}, roční období: Léto")
            elif mesic == 9 or mesic == 10 or mesic == 11:
                print(Fore.GREEN + "Podzim")
                utils.log_to_file(f"Uživatel zadal měsíc {mesic}, roční období: Podzim")
            else:
                print(Fore.RED + "Neplatný měsíc. Zadejte číslo od 1 do 12.")
                utils.log_to_file(f"Uživatel zadal neplatný měsíc: {mesic}")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte číslo.")
            utils.log_to_file("Neplatný vstup při zadávání měsíce.")

def vypis_vsech_cisel():
    """
    Funkce vypíše všechna čísla v zadaném rozsahu.

    Uživatel zadá počáteční a koncové číslo a funkce vypíše všechny čísla v tomto rozsahu (včetně).
    
    :vstup zacatek: Počáteční číslo rozsahu.
    :vstup konec: Konec čísla rozsahu.
    """
    while True:
        try:
            zacatek = int(input("Zadejte počáteční číslo: "))
            konec = int(input("Zadejte koncové číslo: "))
            print(Fore.CYAN + "Všechna čísla v rozsahu:")
            for cislo in range(zacatek, konec + 1):
                print(cislo, end=" ")
            print()
            utils.log_to_file(f"Uživatel zadal rozsah od {zacatek} do {konec}, všechna čísla v rozsahu vypsána.")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání rozsahu čísel.")

def vypis_lichych_cisel():
    """
    Funkce vypíše všechna lichá čísla v zadaném rozsahu.

    Uživatel zadá počáteční a koncové číslo a funkce vypíše pouze lichá čísla v tomto rozsahu.
    
    :vstup zacatek: Počáteční číslo rozsahu.
    :vstup konec: Konec čísla rozsahu.
    """
    while True:
        try:
            zacatek = int(input("Zadejte počáteční číslo: "))
            konec = int(input("Zadejte koncové číslo: "))
            print(Fore.CYAN + "Lichá čísla v rozsahu:")
            for cislo in range(zacatek, konec + 1):
                if cislo % 2 != 0:
                    print(cislo, end=" ")
            print()
            utils.log_to_file(f"Uživatel zadal rozsah od {zacatek} do {konec}, lichá čísla v rozsahu vypsána.")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání rozsahu čísel.")

def vypis_cisel_sestupne():
    """
    Funkce vypíše čísla v sestupném pořadí.

    Uživatel zadá počáteční a koncové číslo, a funkce vypíše čísla v sestupném pořadí mezi těmito dvěma čísly.
    
    :vstup zacatek: Počáteční číslo pro sestupné řazení.
    :vstup konec: Konec čísla pro sestupné řazení.
    """
    while True:
        try:
            zacatek = int(input("Zadejte počáteční číslo: "))
            konec = int(input("Zadejte koncové číslo: "))
            print(Fore.CYAN + "Čísla v sestupném pořadí:")
            for cislo in range(zacatek, konec - 1, -1):
                print(cislo, end=" ")
            print()
            utils.log_to_file(f"Uživatel zadal rozsah od {zacatek} do {konec}, čísla v sestupném pořadí vypsána.")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání rozsahu čísel.")

def vypis_sudych_cisel():
    """
    Funkce vypíše všechna sudá čísla v zadaném rozsahu.

    Uživatel zadá počáteční a koncové číslo a funkce vypíše pouze sudá čísla v tomto rozsahu.
    
    :vstup zacatek: Počáteční číslo rozsahu.
    :vstup konec: Konec čísla rozsahu.
    """
    while True:
        try:
            zacatek = int(input("Zadejte počáteční číslo: "))
            konec = int(input("Zadejte koncové číslo: "))
            print(Fore.CYAN + "Sudá čísla v rozsahu:")
            for cislo in range(zacatek, konec + 1):
                if cislo % 2 == 0:
                    print(cislo, end=" ")
            print()
            utils.log_to_file(f"Uživatel zadal rozsah od {zacatek} do {konec}, sudá čísla v rozsahu vypsána.")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání rozsahu čísel.")

def serazeni_rozsahu():
    """
    Funkce seřadí čísla v zadaném rozsahu vzestupně.

    Uživatel zadá počáteční a koncové číslo a funkce seřadí čísla v tomto rozsahu vzestupně a vypíše je.
    
    :vstup zacatek: Počáteční číslo rozsahu.
    :vstup konec: Konec čísla rozsahu.
    """
    while True:
        try:
            zacatek = int(input("Zadejte počáteční číslo: "))
            konec = int(input("Zadejte koncové číslo: "))
            serazeno = sorted(range(zacatek, konec + 1))
            print(Fore.CYAN + "Seřazený rozsah čísel:")
            print(serazeno)
            utils.log_to_file(f"Uživatel zadal rozsah od {zacatek} do {konec}, seřazený rozsah čísel vypsán.")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání rozsahu čísel.")


def vypis_korekce_poradi():
    """
    Funkce seřadí čísla v zadaném rozsahu a vypíše je v seřazeném pořadí.

    Uživatel zadá počáteční a koncové číslo a funkce seřadí čísla v tomto rozsahu a vypíše je.
    
    :vstup zacatek: Počáteční číslo rozsahu.
    :vstup konec: Konec čísla rozsahu.
    """
    while True:
        try:
            zacatek = int(input("Zadejte počáteční číslo: "))
            konec = int(input("Zadejte koncové číslo: "))
            rozsah = list(range(zacatek, konec + 1))

            rozsah.sort()
            print(Fore.CYAN + "Čísla s automatickou korekcí pořadí:")
            print(rozsah)
            utils.log_to_file(f"Uživatel zadal rozsah od {zacatek} do {konec}, čísla s automatickou korekcí pořadí vypsána.")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání rozsahu čísel.")

def tabulka_nasobeni():
    """
    Funkce vypíše násobilku pro zadané číslo.

    Uživatel zadá číslo, pro které bude vypočítána násobilka (1-10).
    
    :vstup cislo: Číslo, pro které se vypíše násobilka.
    """
    while True:
        try:
            cislo = int(input("Zadejte číslo pro zobrazení násobilky: "))
            print(Fore.CYAN + f"Násobilka čísla {cislo}:")
            for i in range(1, 11):
                print(f"{cislo} x {i} = {cislo * i}")
            utils.log_to_file(f"Uživatel zadal číslo {cislo}, násobilka vypsána.")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání čísla pro násobilku.")

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
    while True:
        try:
            cislo = float(input("Zadejte částku k převodu: "))
            z_mena = input("Zadejte měnu, kterou chcete převést (CZK, EUR, USD): ").upper()
            na_mena = input("Zadejte měnu, na kterou chcete převést (CZK, EUR, USD): ").upper()

            if z_mena in menove_kurzy and na_mena in menove_kurzy:
                prevedena_castka = cislo * (menove_kurzy[na_mena] / menove_kurzy[z_mena])
                print(Fore.CYAN + f"{cislo} {z_mena} je {prevedena_castka:.2f} {na_mena}.")
                utils.log_to_file(f"Uživatel zadal částku {cislo}, měnu {z_mena} a cílovou měnu {na_mena}, převedená částka {prevedena_castka:.2f}.")
                break
            else:
                print(Fore.RED + "Neplatné měny. Zadejte prosím měny z následujících možností: CZK, EUR, USD.")
                utils.log_to_file(f"Uživatel zadal neplatné měny: {z_mena} nebo {na_mena}.")
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím platnou částku.")
            utils.log_to_file("Neplatný vstup při zadávání částky k převodu.")

def hraj_hadej_cislo():
    """
    Funkce implementuje hru "Hádej číslo", kde hráč hádá náhodně vybrané číslo mezi 1 a 100.

    Hráč se pokouší uhodnout číslo. Po každém pokusu mu bude sděleno, zda je zadané číslo
    příliš malé, příliš velké, nebo správné. Hra končí, když hráč uhodne číslo.
    
    :vstup cislo_k_hadani: Náhodně vybrané číslo, které hráč hádá.
    :vstup pokusy: Počet pokusů, které hráč udělal.
    """
    print(Fore.CYAN + "Vítejte ve hře 'Hádej číslo'!")
    cislo_k_hadani = random.randint(1, 100)
    pokusy = 0
    while True:
        try:
            hadane_cislo = int(input("Hádejte číslo mezi 1 a 100: "))
            pokusy += 1
            if hadane_cislo < cislo_k_hadani:
                print(Fore.RED + "Zadané číslo je příliš malé.")
                utils.log_to_file(f"Uživatel zadal číslo {hadane_cislo}, které je příliš malé.")
            elif hadane_cislo > cislo_k_hadani:
                print(Fore.RED + "Zadané číslo je příliš velké.")
                utils.log_to_file(f"Uživatel zadal číslo {hadane_cislo}, které je příliš velké.")
            else:
                print(Fore.GREEN + f"Gratulujeme! Uhodli jste číslo {cislo_k_hadani} za {pokusy} pokusů.")
                utils.log_to_file(f"Uživatel uhodl číslo {cislo_k_hadani} za {pokusy} pokusů.")
                break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím celé číslo.")
            utils.log_to_file("Neplatný vstup při zadávání čísla pro hru 'Hádej číslo'.")

def mark_number_in_list():
    """
    Funkce označí zadané číslo v seznamu čísel.

    Uživatel zadá seznam čísel a číslo, které chce označit. Všechna čísla jsou vypsána
    a číslo, které uživatel zadal, je zvýrazněno vykřičníkem.
    
    :vstup numbers: Seznam čísel, ve kterém se hledá číslo k označení.
    :vstup target: Číslo, které má být označeno v seznamu.
    """
    while True:
        try:
            numbers = input("Zadejte seznam čísel oddělených mezerou: ").split()
            target = int(input("Zadejte číslo, které chcete označit: "))
            for number in numbers:
                if int(number) == target:
                    print(Fore.GREEN + f"{number}!")
                else:
                    print(number)
            utils.log_to_file(f"Uživatel zadal seznam čísel {numbers} a číslo k označení {target}.")
            break
        except ValueError:
            print(Fore.RED + "Neplatný vstup. Zadejte prosím seznam čísel oddělených mezerou.")
            utils.log_to_file("Neplatný vstup při zadávání seznamu čísel nebo cílového čísla.")

def table_of_multiplication():
    """
    Funkce vypíše násobilku pro zadané číslo.

    Uživatel zadá číslo a funkce vypíše jeho násobilku (1 až 10).
    
    :vstup number: Číslo, pro které bude vypočítána násobilka.
    """
    while True:
        try:
            number = int(input("Enter a number for multiplication table: "))
            print(Fore.CYAN + f"Multiplication table of {number}:")
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
            utils.log_to_file(f"Uživatel zadal číslo {number}, násobilka vypsána.")
            break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter an integer.")
            utils.log_to_file("Neplatný vstup při zadávání čísla pro násobilku.")

