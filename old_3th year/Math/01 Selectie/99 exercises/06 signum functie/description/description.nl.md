Programmeer de <a href='https://nl.wikipedia.org/wiki/Signum_(wiskunde)' target='_blanc'>signum</a>-functie:

$$
\text{sgn}: x \mapsto \begin{cases}
-1 & \text{als } x < 0\\
0 & \text{als } x = 0\\
1 & \text{als } x > 0
\end{cases}
$$

De signum functie heeft onderstaande grafiek:

![Signum](media/signum.png "Signum"){:data-caption="De grafiek van de signum functie." width="355px"}

## Opgave
Schrijf een functie `sgn()` die de waarden $$-1$$, $$0$$ en $$1$$ geeft zoals gevraagd.

#### Voorbeelden
```
>>> sgn( 10 )
1
```
```
>>> sgn( 0 )
0
```
```
>>> sgn( -3.1415 )
-1
```