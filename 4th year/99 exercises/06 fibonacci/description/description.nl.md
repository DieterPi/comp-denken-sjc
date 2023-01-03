De <a href="https://nl.wikipedia.org/wiki/Rij_van_Fibonacci" target="_blank">rij van Fibonacci</a> is een gekende getallenrij uit 1202 beschreven in het boek *Liber abaci* (Boek over rekenen).

In de rij komen het eerste en tweede getal overeen met 1. Elk volgende getal wordt gevormd door te som van de twee vorige getallen te nemen. Je krijgt dus een rij als volgt:

$$
1 \quad 1 \quad 2 \quad 3\quad 5\quad 8\quad 13\quad 21 \quad \ldots
$$

![Fibonacci](media/Fibonacci.png "Fibonacci"){:data-caption="De rij van Fibonacci op een postzegel" width="35%"}

## Opgave
Schrijf een functie `fibonnaci()` met het rangnummer als parameter en zodat deze het getal met dat rangnummer retourneert.

#### Voorbeeld
```
>>> fibonnaci( 2 )
1
>>> fibonnaci( 7 )
13
>>> fibonnaci( 50 )
20365011074
```

{: .callout.callout-info}
> #### Tip
> Maak gebruik van de keuzestructuur om de eerste 2 rangnummers apart op te vangen. Gebruik voor de andere getallen hulpvariabelen die telkens de twee laatste getallen bewaren.