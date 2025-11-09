## Gegevens

De hoofdstelling van de rekenkunde is een fundamentele stelling uit de wiskunde. Deze gaat als volgt:

{: .callout.callout-succes}
> #### De hoofdstelling van de rekenkunde
> Elk natuurlijk getal (> 1) dat niet priemgetal is, kan op een unieke manier worden ontbonden als product van priemgetallen (op volgorde na).

Zo geldt bijvoorbeeld dat 60 = 2 · 2 · 3 · 5.

Men kan nu uit elk natuurlijk getal `n` een nieuw getal (we noemen dit het NIO-getal) bepalen volgens de volgend regels:

- Indien het getal priem is, vervang je het getal door `n + 1`
- Indien het getal niet priem is, dan beschouw je de ontbinding in priemfactoren. Vervolgens vervang je in deze vermenigvuldiging elk priemgetal `p` door `p + 1`.
  Zo wordt het NIO-getal van 60 berekend via (2 + 1) · (2 + 1) · (3 + 1) · (5 + 1) = 216.

## Opgave

Vraag een natuurlijk getal aan de gebruiker en bepaal vervolgens het NIO-getal dat gemaakt wordt volgens deze regels.

#### Voorbeelden

Indien de gebruiker `60` intikt, dan verschijnt er:
```
Het NIO-getal van 60 is: 216
```

Indien de gebruiker `7` intikt, dan verschijnt er:
```
Het NIO-getal van 7 is: 8
```

{: .callout.callout-info}
> #### Bron
> Nederlandse Informatica Olympiade 2025-2026