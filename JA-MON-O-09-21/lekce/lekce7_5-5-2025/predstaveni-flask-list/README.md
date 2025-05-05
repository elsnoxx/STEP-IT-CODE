# Ukázka základního použití Flasku – rozšířená verze

Tento projekt slouží jako přehledová ukázka základních i pokročilejších možností frameworku Flask v Pythonu. Najdete zde různé typy rout, práci s parametry, šablonami, formuláři, cookies, soubory, JSON, vlastními hlavičkami a dalšími odpověďmi.

## Co zde najdete

- **Základní routy** (`/`, `/about`)
- **Dynamické routy** s parametry (`/user/<username>`, `/post/<int:post_id>`, `/category/<category>`)
- **Zpracování HTTP metod** (`/login`, `/form`)
- **Práce se šablonami** (`/hello/<name>`)
- **Přesměrování a chybové stránky** (`/redirect`, `/error`, vlastní 404)
- **Různé typy odpovědí** (text, HTML, JSON, tuple, soubor ke stažení, přesměrování, vlastní hlavičky, XML, CSV, cookies, status kódy, tabulka, JavaScript, obrázek, GET/POST parametry, úprava textu)
- **Ukázkový rozcestník** (`/` – index.html) s odkazy na všechny routy

## Jak spustit

1. Ujistěte se, že máte nainstalovaný Python a Flask:
    ```
    pip install flask
    ```

2. Spusťte aplikaci:
    ```
    python app.py
    ```

3. Otevřete prohlížeč a navštivte adresu [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Ukázkové adresy

- `/` – hlavní stránka s rozcestníkem
- `/about` – stránka O nás
- `/user/jmeno` – dynamická adresa s uživatelským jménem
- `/post/5` – dynamická adresa s číslem příspěvku
- `/category/sport` – dynamická adresa s kategorií
- `/login` – ukázka GET/POST (zkuste odeslat formulář)
- `/hello/Tereza` – ukázka šablony (musí být soubor `hello.html` v adresáři `templates`)
- `/form` – ukázka zpracování formuláře
- `/redirect` – přesměrování na hlavní stránku
- `/error` – vyvolání chyby 404
- `/text` – čistý text
- `/html` – HTML odpověď
- `/json` – JSON odpověď
- `/tuple` – tuple odpověď (obsah, status, hlavičky)
- `/download` – stažení souboru
- `/google` – přesměrování na Google
- `/custom` – vlastní status a hlavičky
- `/styled` – HTML s vloženým CSS
- `/plain` – text s content-type
- `/headers` – vlastní hlavičky
- `/xml` – XML odpověď
- `/csv` – CSV odpověď
- `/set-cookie` – nastavit cookie
- `/get-cookie` – získat cookie
- `/status` – prázdná odpověď (204)
- `/json-list` – JSON pole
- `/json-nested` – vnořený JSON
- `/html-table` – HTML tabulka
- `/inline-js` – HTML s JavaScriptem
- `/inline-img` – HTML s obrázkem
- `/params?a=1&b=2` – GET parametry v URL
- `/post-json` – přijmout JSON (POST)
- `/uppercase/ahoj` – převod na velká písmena
- `/repeat/3/flask` – opakování slova

## Šablona hello.html

Vytvořte soubor `hello.html` do složky `templates`:

```html
<!DOCTYPE html>
<html>
  <head><title>Hello</title></head>
  <body>
    <h1>Hello {{ name }}!</h1>
  </body>
</html>
```

## Poznámky

- Všechny routy jsou okomentované přímo v souboru `app.py`.
- Pro testování POST požadavků (např. `/login`, `/form`, `/post-json`) můžete použít formulář na stránce nebo nástroj jako Postman.
- Pro začátečníky je vhodné zkoušet jednotlivé adresy a sledovat, co se děje v prohlížeči.