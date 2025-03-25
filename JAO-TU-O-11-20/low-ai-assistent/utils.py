import os
import prikazy
import sys
from datetime import datetime
from colorama import init

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def zpracuj_prikaz(volba):
    """
    Funkce pro zpracování uživatelského vstupu a volání odpovídající funkce.
    Používá slovník příkazů, kde klíčem je číselná volba uživatele a hodnotou odpovídající funkce.
    
    Pokud uživatel zadá platnou volbu, spustí se odpovídající funkce z modulu `prikazy`.
    Pokud je volba neplatná, zobrazí se chybová zpráva.

    Seznam podporovaných příkazů:
    - "1"  : Určení sudosti nebo lichosti čísla.
    - "2"  : Kontrola, zda je číslo násobkem sedmi.
    - "3"  : Nalezení maximálního čísla ze dvou zadaných.
    - "4"  : Nalezení minimálního čísla ze dvou zadaných.
    - "5"  : Provedení základních aritmetických operací.
    - "6"  : Převod času ze sekund na hodiny, minuty a sekundy.
    - "7"  : Výpočet obvodu a obsahu kruhu.
    - "8"  : Generování náhodného čísla.
    - "9"  : Výpočet ceny na základě zadaných parametrů.
    - "10" : Odhad doby stahování souboru.
    - "11" : Zobrazení pozdravu podle aktuálního času.
    - "12" : Kontrola, zda je číslo šťastné.
    - "13" : Prohození číslic dvouciferného čísla.
    - "14" : Určení ročního období podle měsíce.
    - "15" : Výpis všech čísel v zadaném rozsahu.
    - "16" : Výpis lichých čísel v zadaném rozsahu.
    - "17" : Výpis čísel v sestupném pořadí.
    - "18" : Výpis sudých čísel v zadaném rozsahu.
    - "19" : Seřazení zadaného rozsahu čísel.
    - "20" : Výpis čísel s korekcí pořadí.
    - "21" : Převod měn na základě aktuálního kurzu.
    - "22" : Generování dalšího náhodného čísla.
    - "23" : Hra "Hádej číslo".
    - "24" : Načtení a zobrazení obsahu souboru log.txt.
    - "25" : Ukončení programu.

    :param volba: Řetězec reprezentující volbu uživatele.
    """
    command = {
        "1": prikazy.sudost_lichost,
        "2": prikazy.nasobek_sedmi,
        "3": prikazy.max_dvou_cisel,
        "4": prikazy.min_dvou_cisel,
        "5": prikazy.aritmeticke_operace,
        "6": prikazy.prevod_sekund,
        "7": prikazy.obvod_obsah_kruhu,
        "8": prikazy.generuj_nahodne_cislo,
        "9": prikazy.vypocet_ceny,
        "10": prikazy.doba_stahovani,
        "11": prikazy.casove_pozdravy,
        "12": prikazy.stastne_cislo,
        "13": prikazy.prohozeni_cislic,
        "14": prikazy.rocni_obdobi,
        "15": prikazy.vypis_vsech_cisel,
        "16": prikazy.vypis_lichych_cisel,
        "17": prikazy.vypis_cisel_sestupne,
        "18": prikazy.vypis_sudych_cisel,
        "19": prikazy.serazeni_rozsahu,
        "20": prikazy.vypis_korekce_poradi,
        "21": prikazy.prevod_men,
        "22": prikazy.generuj_nahodne_cislo,
        "23": prikazy.hraj_hadej_cislo,
        "24": read_from_file,
        "25": sys.exit(0)
    }

    if volba in command:
        command[volba]()
    else:
        print(Fore.RED + "Neplatna volba")
    


def log_to_file(message):
    """
    Funkce pro zápis zprávy do souboru log.txt.
    Přidá časovou značku k zprávě a zapíše ji do souboru.
    Formátování data a času na formát 'YYYY-MM-DD HH:MM:SS'
    """
    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f"{date}: {message}" + '\n')
        f.close()

def read_from_file():
    """
    Funkce pro čtení obsahu souboru 'log.txt' a jeho výpis do konzole.
    """