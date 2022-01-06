## Opgave
In 1741 lostte Euler het beroemde [Bazel-probleem](https://nl.wikipedia.org/wiki/Bazel-probleem) op. Hij bewees dat de (oneindige) som van de omgekeerden van de kwadraten van de natuurlijke getallen gelijk is aan $$\frac{\pi^2}{6}$$, met andere woorden:

$$
\dfrac{\pi^2}{6} = \dfrac{1}{1^2}+\dfrac{1}{2^2}+\dfrac{1}{3^2}+\dfrac{1}{4^2}+\ldots
$$

Je kan deze uitdrukking omvormen om de waarde van π te berekenen (in de praktijk: *benaderen*)

$$
\pi = \sqrt{6\cdot \left( \dfrac{1}{1^2}+\dfrac{1}{2^2}+\dfrac{1}{3^2}+\dfrac{1}{4^2}+\ldots \right)}
$$

Vul de functie `bazel_benadering()` aan met als parameter het aantal termen dat in de som berekend worden die een benadering bepaalt voor de waarde van π. 

#### Voorbeelden