from colorama import Fore

def zobraz_menu(vybrana_volba=None):
    """
    Funkce zobrazí menu s možnostmi pro uživatele. Pokud je zadaná volba, zvýrazní ji v menu.

    :param vybrana_volba: Volitelný argument, číslo volby, která má být zvýrazněna.
    """
    menu = """
    1. Určení sudosti nebo lichosti čísla.
    2. Kontrola, zda je číslo násobkem sedmi.
    3. Nalezení maximálního čísla ze dvou zadaných.
    4. Nalezení minimálního čísla ze dvou zadaných.
    5. Provedení základních aritmetických operací.
    6. Převod času ze sekund na hodiny, minuty a sekundy.
    7. Výpočet obvodu a obsahu kruhu.
    8. Generování náhodného čísla.
    9. Výpočet ceny na základě zadaných parametrů.
    10. Odhad doby stahování souboru.
    11. Zobrazení pozdravu podle aktuálního času.
    12. Kontrola, zda je číslo šťastné.
    13. Prohození číslic dvouciferného čísla.
    14. Určení ročního období podle měsíce.
    15. Výpis všech čísel v zadaném rozsahu.
    16. Výpis lichých čísel v zadaném rozsahu.
    17. Výpis čísel v sestupném pořadí.
    18. Výpis sudých čísel v zadaném rozsahu.
    19. Seřazení zadaného rozsahu čísel.
    20. Výpis čísel s korekcí pořadí.
    21. Převod měn na základě aktuálního kurzu.
    22. Generování dalšího náhodného čísla.
    23. Hra "Hádej číslo".
    24. Načtení a zobrazení obsahu souboru log.txt.
    25. Ukončení programu.
    """
    print(Fore.RESET, end="")
    if vybrana_volba:
        menu_list = menu.splitlines()
        for i in range(len(menu_list)):
            if i == int(vybrana_volba):
                print(Fore.GREEN + menu_list[i])
            else:
                print(Fore.RESET + menu_list[i])
    else:
        print(menu)