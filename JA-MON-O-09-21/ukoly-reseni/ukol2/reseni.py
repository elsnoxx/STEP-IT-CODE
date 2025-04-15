# ==============================================================================================================
# Úkol 1: Součet nebo součin tří čísel
# Popis: Uživatel zadá tři čísla. Program na základě volby uživatele vypočítá součet nebo součin těchto čísel 
# a výsledek vypíše.
# ==============================================================================================================

# Získání tří čísel od uživatele
print("Zadejte tři čísla:")
num1 = float(input("První číslo: "))
num2 = float(input("Druhé číslo: "))
num3 = float(input("Třetí číslo: "))

# Získání volby od uživatele
print("Zvolte operaci:")
print("1 - Součet")
print("2 - Součin")
choice = input("Vaše volba: ")

# Výpočet na základě volby
if choice == "1":
    result = num1 + num2 + num3
    print("Součet zadaných čísel je:", result)
elif choice == "2":
    result = num1 * num2 * num3
    print("Součin zadaných čísel je:", result)
else:
    print("Neplatná volba!")

# ==============================================================================================================
# Úkol 2: Maximum, minimum nebo průměr
# Popis: Uživatel zadá tři čísla. Program na základě volby uživatele vypíše maximum, minimum nebo aritmetický 
# průměr těchto tří čísel.
# ==============================================================================================================

# Získání tří čísel od uživatele
print("\nZadejte tři čísla:")
num1 = float(input("První číslo: "))
num2 = float(input("Druhé číslo: "))
num3 = float(input("Třetí číslo: "))

# Získání volby od uživatele
print("Zvolte operaci:")
print("1 - Maximum")
print("2 - Minimum")
print("3 - Aritmetický průměr")
choice = input("Vaše volba: ")

# Výpočet na základě volby
if choice == "1":
    result = max(num1, num2, num3)
    print("Maximum zadaných čísel je:", result)
elif choice == "2":
    result = min(num1, num2, num3)
    print("Minimum zadaných čísel je:", result)
elif choice == "3":
    result = (num1 + num2 + num3) / 3
    print("Aritmetický průměr zadaných čísel je:", result)
else:
    print("Neplatná volba!")

# ==============================================================================================================
# Úkol 3: Převod metrů podle volby
# Popis: Uživatel zadá hodnotu v metrech a zvolí si, na jakou jednotku ji chce převést. Na výběr jsou míle, 
# palce a yardy. Program provede příslušný převod a výsledek zobrazí.
# ==============================================================================================================

# Získání délky v metrech od uživatele
length_meters = float(input("\nZadejte délku v metrech: "))

# Získání volby od uživatele
print("Zvolte jednotku pro převod:")
print("1 - Míle")
print("2 - Palce")
print("3 - Yardy")
choice = input("Vaše volba: ")

# Převod na základě volby
if choice == "1":
    result = length_meters * 0.000621371
    print("Délka v mílích je:", result)
elif choice == "2":
    result = length_meters * 39.3701
    print("Délka v palcích je:", result)
elif choice == "3":
    result = length_meters * 1.09361
    print("Délka ve yardech je:", result)
else:
    print("Neplatná volba!")