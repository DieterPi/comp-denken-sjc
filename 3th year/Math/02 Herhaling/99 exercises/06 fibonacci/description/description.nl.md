De rij van Fibonacci is een gekende getallenrij waarvan de eerste en de tweede waarde overeenkomen met 1. Elk volgende getal wordt gevormd door te som van de twee vorige getallen te nemen. Je krijgt dus een rij als volgt:

$$
1 \quad 1 \quad 2 \quad 3\quad 5\quad 8\quad 13\quad 21 \quad \ldots
$$

## Opgave
Schrijf een functie `fibonnaci()` met het rangnummer als parameter en het desbetreffende getal retourneert.

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