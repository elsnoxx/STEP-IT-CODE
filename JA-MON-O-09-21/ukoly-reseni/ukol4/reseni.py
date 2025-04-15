import random  # Importujeme modul random pro generování náhodných čísel

# ==============================================================================================================
# Třída BankovniUcet
# Popis: Třída reprezentuje bankovní účet s atributy pro majitele, číslo účtu a zůstatek. Obsahuje metody pro
# vklad, výběr, přičtení úroku a výpis informací o účtu.
# ==============================================================================================================

class BankovniUcet:
    def __init__(self, jmeno, cislo_uctu, zustatek):
        """
        Konstruktor třídy BankovniUcet.
        Inicializuje jméno majitele, číslo účtu a počáteční zůstatek.
        """
        self.jmeno = jmeno
        self.cislo_uctu = cislo_uctu
        self.zustatek = zustatek

    def vklad(self, castka):
        """
        Metoda pro vklad peněz na účet.
        Přičte zadanou částku ke zůstatku.
        """
        self.zustatek += castka

    def vyber(self, castka):
        """
        Metoda pro výběr peněz z účtu.
        Odečte zadanou částku od zůstatku, pokud je dostatek prostředků.
        """
        if castka <= self.zustatek:
            self.zustatek -= castka
        else:
            print(f"Chyba: Nedostatek prostředků na účtu {self.cislo_uctu}.")

    def urok(self):
        """
        Metoda pro přičtení úroku k zůstatku.
        Úrok je pevně stanoven na 3 %.
        """
        self.zustatek *= 1.03

    def vypis(self):
        """
        Metoda pro výpis informací o účtu.
        Zobrazí jméno majitele, číslo účtu a aktuální zůstatek.
        """
        print(f"Majitel: {self.jmeno}, Číslo účtu: {self.cislo_uctu}, Zůstatek: {self.zustatek:.2f} Kč")


# ==============================================================================================================
# Vytvoření seznamu účtů
# Popis: Vytvoříme seznam `banka`, který obsahuje 10 instancí třídy BankovniUcet s různými daty.
# ==============================================================================================================

banka = [
    BankovniUcet("Jan Novák", "1234567890", 1000),
    BankovniUcet("Petr Svoboda", "2345678901", 2000),
    BankovniUcet("Eva Dvořáková", "3456789012", 1500),
    BankovniUcet("Marie Černá", "4567890123", 3000),
    BankovniUcet("Karel Veselý", "5678901234", 2500),
    BankovniUcet("Lucie Malá", "6789012345", 1800),
    BankovniUcet("Tomáš Krátký", "7890123456", 2200),
    BankovniUcet("Anna Velká", "8901234567", 1700),
    BankovniUcet("Marek Novotný", "9012345678", 2600),
    BankovniUcet("Jana Horáková", "0123456789", 3100),
]

# ==============================================================================================================
# Operace s účty
# Popis: Provedeme různé operace s účty podle zadání.
# ==============================================================================================================

# 1. Každému účtu přidáme 500 Kč
for ucet in banka:
    ucet.vklad(500)

# 2. U prvního, třetího a posledního účtu provedeme výběr 250 Kč
banka[0].vyber(250)
banka[2].vyber(250)
banka[-1].vyber(250)

# 3. U ostatních účtů provedeme výběr náhodné částky v rozmezí 100 až 300 Kč
for i, ucet in enumerate(banka):
    if i not in [0, 2, len(banka) - 1]:  # Vynecháme první, třetí a poslední účet
        nahodna_castka = random.randint(100, 300)
        ucet.vyber(nahodna_castka)

# 4. U všech účtů přičteme úrok
for ucet in banka:
    ucet.urok()

# 5. Vypíšeme informace o všech účtech
print("\nInformace o všech účtech po provedení operací:")
for ucet in banka:
    ucet.vypis()