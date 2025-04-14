# 🛰️ Aplikace pro sledování ISS a lidí ve vesmíru

## 🎯 Cíl
Vytvoř konzolovou Python aplikaci, která bude pracovat s veřejnými API pro získání:
- aktuálních informací o Mezinárodní vesmírné stanici (ISS)
- seznamu osob nacházejících se právě ve vesmíru

---

## 🔧 Požadavky
- Použij knihovnu `requests` pro práci s HTTP požadavky
- Ošetři **chybný vstup** (např. neplatná volba v menu)
- Přehledně vypisuj výsledky:
  - jména osob
  - souřadnice ISS (zeměpisná délka a šířka)
- Program běží opakovaně, dokud uživatel nezvolí možnost **3 – Konec**

---

## 🌟 Bonusové úkoly
- Převod časového razítka (timestamp) na čitelný formát pomocí `datetime`
- Zobrazení souřadnic ISS na **jednoduché mapě** pomocí knihovny `folium` *(volitelné)*

---

## 🧭 Funkce aplikace
Po spuštění nabídne aplikace uživateli jednoduché textové menu:

```
1 – Zobrazit aktuální polohu ISS  
2 – Zobrazit seznam lidí ve vesmíru  
3 – Konec  
```

---

## 🌐 Použitá API

### 1. Aktuální poloha ISS  
- **URL:** `http://api.open-notify.org/iss-now.json`  
- **Popis:** Vrací aktuální zeměpisnou šířku a délku ISS.

### 2. Lidé ve vesmíru  
- **URL:** `http://api.open-notify.org/astros.json`  
- **Popis:** Vrací seznam všech lidí aktuálně ve vesmíru (jména + kosmické lodě)

---

📚 Materiály z lekce: [elsnoxx.github.io](https://elsnoxx.github.io)  
📤 Výslednou aplikaci odevzdejte do systému **MyStat**.
