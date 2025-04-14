from colorama import Fore

def zobraz_menu(vybrana_volba=None):
    """
    Funkce zobrazí menu s možnostmi pro uživatele. Pokud je zadaná volba, zvýrazní ji v menu.

    :param vybrana_volba: Volitelný argument, číslo volby, která má být zvýrazněna.
    """
    menu = """
    1. Zjistit, zda je číslo sudé nebo liché
    2. Zkontrolovat, zda je číslo násobkem 7
    3. Zjistit maximum ze dvou čísel
    4. Zjistit minimum ze dvou čísel
    5. Provést aritmetické operace (+, -, *, /)
    6. Převést sekundy na hodiny, minuty a sekundy
    7. Spočítat obvod a obsah kruhu
    8. Generovat náhodné číslo
    9. Vypočítat cenu objednávky
    10. Spočítat dobu stahování souboru
    11. Vytvořit časový pozdrav
    12. Zkontrolovat, zda je číslo šťastné
    13. Prohodit první a poslední číslici čísla
    14. Zjistit roční období podle měsíce
    15. Vypisovat všechny čísla v rozsahu
    16. Vypisovat lichá čísla v rozsahu
    17. Vypisovat čísla v sestupném pořadí
    18. Vypisovat sudá čísla v rozsahu
    19. Seřadit rozsah čísel
    20. Vypisovat čísla s automatickou korekcí pořadí
    21. Převod mezi měnami
    22. Vygenerovat náhodné číslo (opět)
    23. Hrát hru "Hádej číslo"
    24. Výpis logu ze souboru
    25. Konec
    """

    if vybrana_volba:
        menu_lines = menu.splitlines()
        for i in range(len(menu_lines)):
            if i == int(vybrana_volba):
                print(Fore.GREEN + menu_lines[i])
            else:
                print(Fore.RESET + menu_lines[i])
    else:
        print(menu)