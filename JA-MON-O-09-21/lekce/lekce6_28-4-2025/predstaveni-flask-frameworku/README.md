# Ukázka základního použití Flasku

Tento projekt slouží jako demonstrace základních principů frameworku Flask v Pythonu.

## Co zde najdete

- **Základní routy** (`/`, `/about`)
- **Dynamické routy** s parametry (`/user/<username>`, `/post/<int:post_id>`, `/category/<category>`)
- **Zpracování HTTP metod** (`/login`, `/form`)
- **Práce se šablonami** (`/hello/<name>`)
- **Přesměrování a chybové stránky** (`/redirect`, `/error`)

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

- `/` – hlavní stránka
- `/about` – stránka O nás
- `/user/jmeno` – dynamická adresa s uživatelským jménem
- `/post/5` – dynamická adresa s číslem příspěvku
- `/category/sport` – dynamická adresa s kategorií
- `/login` – ukázka GET/POST (zkuste odeslat formulář)
- `/hello/Tereza` – ukázka šablony (musí být soubor `hello.html` v adresáři `templates`)
- `/form` – ukázka zpracování formuláře
- `/redirect` – přesměrování na hlavní stránku
- `/error` – vyvolání chyby 404

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