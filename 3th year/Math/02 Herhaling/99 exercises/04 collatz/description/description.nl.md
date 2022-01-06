Het [vermoeden van Collatz](https://nl.wikipedia.org/wiki/Vermoeden_van_Collatz) is een vermoeden (dus nog **niet** bewezen) uit 1937 dat zegt dat een bepaalde *iteratieve* methode steeds bij 1 eindigt. De methode verloopt als volgt:

Neem een willeurig geheel getal $$n$$ als startwaarde:

- als $$n$$ even is, deel het door 2.
- als $$n$$ oneven is, vermenigvuldig het met 3 en tel er 1 bij op.

Als $$n= 12$$ dan verkrijg je de volgende rij: $$12, 6, 3, 10, 5, 16, 8, 4, 2, 1$$. Je merkt dat de rij inderdaad eindigt bij $$1$$

![Collatz conjecture](media/collatz_conjecture.png "Collatz conjecture"){:data-caption="De hypothese van Collatz, xkcd-cartoon (https://xkcd.com/710)" width="30%"}

## Opgave
In deze oefening schrijf je 2 functies. De functie `volgend_collatz_getal()` die gegeven een getal het volgende getal in de rij berekent. 
Daarnaast schrijf je een functie `collatz()` die gegeven een startwaarde de volledige rij (tot aan 1) bepaalt. Maak in deze functie gebruik van de vorige functie `volgend_collatz_getal()`.

#### Voorbeeld
```
>>> volgend_collatz_getal( 8 )
4
>>> volgend_collatz_getal( 17 )
52

>>> collatz(8)
[8, 4, 2, 1]
>>> collatz(17)
[17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```
{: .callout.callout-info}
> #### Tip
> Gebruik de gehele deling `//`.
> Sla de rij op in een lijst en gebruik telkens de `.append()` methode.