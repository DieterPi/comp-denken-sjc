De Italiaanse wiskundige <a href="https://nl.wikipedia.org/wiki/Rafael_Bombelli" target="_blank">Raphael Bombelli</a> (16e eeuw) bedacht een methode om de vierkantswortel van een natuurlijk getal te berekenen (of beter, te benaderen). De methode werkt als volgt. 

Stel dat we de $$\mathsf{x = \sqrt{19}}$$ willen uitrekenen, dan geldt sowieso dat $$\mathsf{x^2 = 16+3 = 4^2+3}$$ of dus 

$$
\mathsf{\begin{array}{rrcl}
& x^2 - 4^2 & = & 3 \\
\Leftrightarrow & (x-4) \cdot (x+4) & = & 3\\
\Leftrightarrow & x- 4 & = & \dfrac{3}{x+4}\\
\Leftrightarrow & x & = & 4+\dfrac{3}{x+4} = 4 + \dfrac{3}{4+x}\end{array}}
$$

En nu begint de pret 😎, het is namelijk mogelijk om de $$\mathsf{x}$$ in de breuk te vervangen door het ganse rechterlid. Zodat

$$
\mathsf{
\begin{array}{rrcl}
& x & = & 4+\dfrac{3}{4+x}\\
\Leftrightarrow & x & = & 4 + \dfrac{3}{4 + {\color{#0061A6}4 + \frac{3}{4+x}}}\\
\Leftrightarrow & x & = & 4 + \dfrac{3}{8+\frac{3}{4+4+\frac{3}{4+x}}}\\
\Leftrightarrow & x & = & 4 + \dfrac{3}{8+\frac{3}{8+\frac{3}{4+\ldots}}}\\
\end{array}}
$$

hetgeen men een kettingbreuk noemt.

Dit kan je gebruiken om $$\mathsf{\sqrt{19}}$$ te benaderen, door in het recherlid $$\mathsf{x}$$ te vervangen door zijn meest eenvoudige benadering: 4, met andere woorden:

$$
\mathsf{4, \qquad 4+\dfrac{3}{8}, \qquad 4+\dfrac{3}{8+\frac{3}{8}}, \qquad 4+\dfrac{3}{8+\frac{3}{8+\ldots}}}
$$

zijn telkens nauwkeurigere benaderingen voor $$\mathsf{\sqrt{19}}$$. 

## Opgave
Schrijf een programma dat een natuurlijk getal en vervolgens het aantal kettingbreuken aan de gebruiker vraagt. Vervolgens bereken je de benadering voor deze hoeveelheidkettingbreuken. Rond steeds af op **zes decimalen**.

#### Voorbeelden
Bij de invoer `19` en `3` verkrijg je:
```
De benadering met 3 kettingbreuken is 4.358929
```

Bij de invoer `19` en `0` verkrijg je:
```
De benadering met 3 kettingbreuken is 4
```

{: .callout.callout-info}
> #### Tip
> Voer deze berekening eens uit op papier. Denk goed na over hoe je deze kettingbreuken manueel uitrekent, je zal Python dit op dezelfde manier moeten laten doen.