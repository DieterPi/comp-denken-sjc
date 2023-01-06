De sneeuwvlok van Koch is een <a href="https://nl.wikipedia.org/wiki/Fractal" target="_blank">fractaal</a> die gevormd wordt door elke zijde van een gelijkzijdige driehoek in drie delen te verdelen en nadien op het middelste deel opnieuw een gelijkzijdige driehoek te tekenen. Dit proces oneindig lang uitvoeren resulteert in een figuur die er als een sneeuwvlok uitziet.

Het was wiskundige <a href="https://nl.wikipedia.org/wiki/Helge_von_Koch" target="_blank">Helge von Koch</a> die zijn naam gaf aan deze fractaal.

![Vorming van Koch's sneeuwvlok.](media/jessica-lewis.jpg "Afbeelding door António Miguel de Campos op Wikimedia."){:data-caption="Vorming van Koch's sneeuwvlok." width="300px"}

De oppervlakte van de sneeuwvlok kan berekend worden met onderstaande formule:

$$
A = \dfrac{2\cdot z^2 \cdot \sqrt{3}}{5}
$$

waarbij $$z$$ de zijde van de oorspronkelijke gelijkzijdige driehoek voorstelt.

## Opgave
Schrijf een functie `oppervlakte_koch( z )` die de oppervlakte van de sneeuwvlak van Koch berekent en **afdrukt**. Rond af op 2 cijfers.

#### Voorbeeld
```
>>> oppervlakte_koch( 2 )
2.77
```