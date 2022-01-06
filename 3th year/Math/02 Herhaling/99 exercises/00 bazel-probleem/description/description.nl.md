In 1741 lostte [Euler](https://nl.wikipedia.org/wiki/Leonhard_Euler) het beroemde [Bazel-probleem](https://nl.wikipedia.org/wiki/Bazel-probleem) op. 

![Euler](media/Euler.jpg "Euler"){:data-caption="Je nieuwe held, Leonhard Euler" width="28%"}

Hij bewees dat de (oneindige) som van de omgekeerden van de kwadraten van de natuurlijke getallen gelijk is aan $$\frac{\pi^2}{6}$$, met andere woorden:

$$
\dfrac{\pi^2}{6} = \dfrac{1}{1^2}+\dfrac{1}{2^2}+\dfrac{1}{3^2}+\dfrac{1}{4^2}+\ldots
$$

Je kan deze uitdrukking omvormen om de waarde van π te berekenen (in de praktijk: *benaderen*)

$$
\pi = \sqrt{6\cdot \left( \dfrac{1}{1^2}+\dfrac{1}{2^2}+\dfrac{1}{3^2}+\dfrac{1}{4^2}+\ldots \right)}
$$

## Opgave

Bepaal een benadering voor het getal π met bovenstaande uitdrukking. Vul hiervoor onderstaande functie `bazel_benadering()` aan. De parameter stelt het aantal termen in de som voor. Rond de benadering af op 12 cijfers na de komma.

#### Voorbeelden
Zoals je in onderstaande voorbeelden merkt moeten er vrij veel termen berekend opdat de benadering in de buurt komt, gelukkig kan een computer dit vrij vlot.
```
>>> bazel_benadering(10)
3.049361636
>>> bazel_benadering(100)
3.132076532
>>> bazel_benadering(10000)
3.141497164
```