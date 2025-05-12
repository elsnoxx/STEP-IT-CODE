# Pokémon vyhledávač – Flask webová aplikace

Tato aplikace umožňuje vyhledávat informace o Pokémonech pomocí [PokéAPI](https://pokeapi.co/). Uživatel zadá jméno Pokémona do formuláře a aplikace zobrazí jeho obrázek, základní vlastnosti (výška, váha), typy a schopnosti.

## Funkce

- Vyhledávání Pokémona podle jména (např. "pikachu", "bulbasaur").
- Zobrazení obrázku Pokémona.
- Výpis základních údajů: výška, váha, typy, schopnosti.
- Ošetření chyb (Pokémon nenalezen).
- Jednoduché a přehledné rozhraní.

## Jak spustit

1. Ujistěte se, že máte nainstalovaný Python a knihovny Flask a requests:
    ```
    pip install flask requests
    ```

2. Spusťte aplikaci:
    ```
    python app.py
    ```

3. Otevřete prohlížeč a navštivte adresu [http://127.0.0.1:5000/pokemon](http://127.0.0.1:5000/pokemon)

## Struktura projektu

```
pokemon-web/
├── app.py
├── templates/
│   └── pokemon.html
└── README.md
```

## Inspirace a rozšíření

- Můžete přidat vyhledávání podle ID, výpis statistik, evoluční řetězec, seznam všech Pokémonů, filtrování podle typu a další funkce.
- Více informací najdete na [https://pokeapi.co/](https://pokeapi.co/).

---