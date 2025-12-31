Eendjes vissen is een gekend spel van op de kermis. De eendjes komen een per een voorbij en de speler kan er een aantal uit vissen. Elk eendje
heeft als waarde een geheel getal tussen 1 en 5. In deze opgave wordt een variant op het klassieke eendjes vissen beschouwd. De speler ziet op
voorhand de waarden van alle eendjes die voorbij komen en moet per spel vier opeenvolgende eendjes selecteren om een zo hoog mogelijke score te
behalen.

![Foto door Renaud Confavreux op Unsplash.](media/renaud-confavreux.jpg "Foto door Renaud Confavreux op Unsplash."){:data-caption="Foto door Renaud Confavreux op Unsplash." width="30%"}

Bijvoorbeeld, uit de reeks bestaande uit 10 eendjes met waarden 5, 2, 4, 1, 1, 5, 4, 4, 3, 2 moet de speler de vier eendjes vanaf **positie 6** vissen om de hoogste score te behalen (5 + 4 + 4 + 3 = 16).

## Opgave
Schrijf een functie `bepaal_nummer(eendjes)` die de positie van het eerste eendje retourneert zodat dit samen met de drie opeenvolgende eendjes de hoogste score bepaalt.

Als meerdere beginposities dezelfde score als resultaat geven dan wordt de eerste van deze beginposities geretourneerd.

#### Voorbeelden

```python
>>> bepaal_nummer([5, 2, 4, 1, 1, 5, 4, 4, 3, 2])
6
```

{: .callout.callout-secondary}
>#### Bron
> Dit is een oefening uit de Vlaamse programmeerwedstrijd 2014 - categorie 1.