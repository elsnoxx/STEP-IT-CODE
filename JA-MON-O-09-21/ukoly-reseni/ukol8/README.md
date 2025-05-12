# Vizualizace dat z veřejného API – ISS (Mezinárodní vesmírná stanice)

## Zadání úkolu

V tomto úkolu si vyzkoušíš, jak získat data z veřejného API, zpracovat je v Pythonu a zobrazit na webové stránce pomocí Flasku. Konkrétně budeš pracovat s API, které poskytuje informace o aktuální poloze Mezinárodní vesmírné stanice (ISS) a o lidech, kteří jsou právě ve vesmíru.

---

## Co budeš dělat

1. **Stáhneš data z veřejného API**  
   Použiješ API [open-notify.org](http://open-notify.org/), které nabízí:
   - Aktuální polohu ISS (`/iss-now.json`)
   - Seznam lidí ve vesmíru (`/astros.json`)

2. **Vytvoříš jednoduchou Flask aplikaci**
   - V souboru `app.py` stáhneš data z API pomocí knihovny `requests`.
   - Data zpracuješ a předáš do HTML šablony.

3. **Vytvoříš HTML šablonu**
   - V souboru `templates/index.html` zobrazíš:
     - Aktuální čas, zeměpisnou šířku a délku ISS.
     - Mapu s aktuální polohou ISS (např. pomocí Google Maps iframe).
     - Seznam lidí, kteří jsou právě ve vesmíru, včetně jejich jména a vesmírné lodi/station.
   - **Použij tyto URL adresy pro dotazování na data:**
     - Aktuální poloha ISS: `http://api.open-notify.org/iss-now.json`
     - Seznam lidí ve vesmíru: `http://api.open-notify.org/astros.json`

---

## Postup

1. **Nainstaluj potřebné knihovny:**
```
pip install flask requests
```

2. **Vytvoř soubor `app.py`**  
Tento soubor bude obsahovat logiku pro získání dat z API a jejich předání do šablony.

3. **Vytvoř složku `templates` a do ní soubor `iss.html`**  
V této šabloně zobrazíš získaná data přehledně uživateli.

4. **Spusť aplikaci:**
```
python app.py
```

A otevři stránku [http://localhost:5000](http://localhost:5000) ve svém prohlížeči.

---

## Co si procvičíš

- Práci s veřejným API (HTTP požadavky, JSON data)
- Základy webového frameworku Flask
- Předávání dat do HTML šablony a jejich vizualizaci
- Základy práce s mapou v HTML (iframe)

---

## Bonus

- Zobraz na mapě i další informace (např. popisek s časem).
- Přidej automatické obnovení dat (např. každých 30 sekund pomocí JavaScriptu).

---

**Hodně štěstí!**