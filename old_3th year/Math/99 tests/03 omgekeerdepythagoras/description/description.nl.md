Indien drie lengtes gegeven worden kan je eenvoudig nagaan of de driehoek rechthoekig is met de omgekeerde stelling van Pythagoras.

{: .callout.callout-secondary}
> #### Omgekeerde stelling van Pythagoras
> Als in een driehoek het kwadraat van een zijde gelijk is aan de som van de kwadraten van de andere zijden, dan is deze rechthoekig.

## Opgave
Schrijf een functie `rechthoekig()` met drie zijden als parameter die nagaat of een driehoek al dan niet rechthoekig is.

#### Voorbeelden
```
>>> rechthoekig( 3, 4 ,5 )
De driehoek is rechthoekig.
```
```
>>> rechthoekig( 5, 4, 5 )
De driehoek is niet rechthoekig.
```

{: .callout.callout-info}
> #### Tip
> Het kwadraat van een getal kan je op drie manieren laten berekenen. Met behulp van de `pow()` functie, zoals `pow( a, 2 )` of via de definite `a*a` of met de verkorte notatie `a**2`
