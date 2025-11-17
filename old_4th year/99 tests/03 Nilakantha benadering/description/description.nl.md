Het is een illusie om te denken dat de meeste ontwikkelingen in de wiskunde zich enkel in het Westen hebben afgespeeld. Heel wat Oosterse wijsheren leverenden belangrijke bijdragen. Zo ook de Indische wiskunde, astronoom en filosoof <a href='https://nl.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz' target='_blanc'>Nilakantha Somayaji</a> die in de 15e eeuw onderstaande (alternerende) formule publiceerde:

![Keļallur Nilakantha Somayaji.](media/Nilakantha.jpg "Keļallur Nilakantha Somayaji"){:data-caption="Keļallur Nilakantha Somayaji." width="20%"}

$$
\dfrac{\pi-3}{4} = \dfrac{1}{2 \cdot 3\cdot 4} - \dfrac{1}{4 \cdot 5\cdot 6} +\dfrac{1}{6 \cdot 7\cdot 8} -\ldots
$$

Door de formule wat om te vormen vinden we een benadering voor π.

$$
\pi = 3+4 \cdot \left( \dfrac{1}{2 \cdot 3\cdot 4} - \dfrac{1}{4 \cdot 5\cdot 6} +\dfrac{1}{6 \cdot 7\cdot 8} -\ldots\right)
$$

## Opgave

Bepaal een benadering voor het getal π met bovenstaande uitdrukking. Vul hiervoor onderstaande functie `nilakantha_benadering()` aan. De parameter stelt het aantal termen in de som voor. Rond de benadering steeds af op 9 cijfers na de komma.

#### Voorbeelden
Deze methode werkt vrij snel, wiskundig zegt men dat deze snel *convergeert* naar de echte waarde van π.
```
>>> nilakantha_benadering( 10 )
3.141406718
```
```
>>> nilakantha_benadering( 100 )
3.141592411
```
```
>>> nilakantha_benadering( 10000 )
3.141592654
```

{: .callout.callout-info}
> #### Tip
> Het alterneren kan je gemakkelijk bekomen via `pow( -1, i )`. Als `i` even is zal dit `1` opleveren, is `i` oneven dan levert dit `-1` op.