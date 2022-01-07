Programmeer de <a href='https://nl.wikipedia.org/wiki/Signum_(wiskunde)' target='_blanc'>signum</a>-functie:

$$
\text{sgn}: x \mapsto \begin{cases}
-1 & \text{als } x < 0\\
0 & \text{als } x = 0\\
1 & \text{als} x > 0
\end{cases}
$$

## Opgave
Schrijf een functie `sgn()` die de waarden -1, 0 en 1 retourneert zoals gevraagd.

#### Voorbeeld
```
>>> ct_treshold(15)
sterk positief
>>> ct_treshold(20.2)
gewoon positief
```