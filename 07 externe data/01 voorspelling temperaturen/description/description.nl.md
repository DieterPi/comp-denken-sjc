Hoe warm of hoe koud wordt het de komende uren?

![Foto door Vladimir Srajber op Pexels.](media/vladimirsrajber.jpg "Foto door Vladimir Srajber op Pexels."){:data-caption="Foto door Vladimir Srajber op Pexels." width="40%"}

De meeste weermodellen slagen er goed in om de temperaturen in de nabije toekomst nauwkeurig te voorspellen. Via onderstaande code wordt een lijst opgehaald met alle temperatuurvoorspellingen binnen Aalst in de komende uren.

Zo zal de variabele `temperaturen` een lijst bevatten van de vorm: `[16.1, 17.2, 15.1, 14.2, 15.0, ..., 20.2]`. Elk element stelt de voorspelde temperatuur voor op een bepaald uur sinds middernacht. Het eerste element hoort dus bij 0 uur, het tweede bij 1 uur, enzovoort...

## Gevraagd
Vraag een **doeltemperatuur** aan de gebruiker. Onderzoek daarna met behulp van de lijst temperaturen na hoeveel uur deze temperatuur voor het eerst bereikt wordt.

- Tel hierbij vanaf middernacht.
- Indien de temperatuur niet voorkomt in de lijst, meld je dat deze temperatuur in de nabije toekomst niet bereikt wordt.

#### Voorbeelden
Bij een invoer van `15.0` kan er verschijnen:

```
De temperatuur 15.0 °C wordt bereikt na 16 uren.
```

Bij een invoer van `40.0` kan er verschijnen:

```
De temperatuur 40.0 °C wordt in de nabije toekomst niet bereikt.
```