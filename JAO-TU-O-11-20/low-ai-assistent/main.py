import os
import menu
import utils
from colorama import Fore, Style, init

# Inicializace colorama pro automatické resetování barev
init(autoreset=True)

def main():
    # Vyčistí konzoli (pokud je to implementováno v utils)
    utils.clear_console()

    # Vytiskne úvodní pozdrav
    print(Fore.CYAN + "Hello, I am your AI assistant. How can I help you?\n")

    while True:
        # Zobrazení menu
        menu.zobraz_menu()

        # Uživatelský vstup pro výběr příkazu
        volba = input(Fore.YELLOW + "Zadejte číslo příkazu: ")

        # Zaloguje uživatelský vstup
        utils.log_to_file(f"Uživatel zadal příkaz: {volba}")
        
        # Vyčistí konzoli po zadání volby
        utils.clear_console()

        # Zobrazení menu s vybranou volbou
        menu.zobraz_menu(volba)

        # Zavolá funkci pro zpracování příkazu
        utils.zpracuj_prikaz(volba)

if __name__ == "__main__":
    main()
