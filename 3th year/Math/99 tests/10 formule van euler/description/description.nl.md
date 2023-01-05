In de 18e eeuw ontdekte <a href="https://nl.wikipedia.org/wiki/Leonhard_Euler" target="_blank">Leonard Euler</a> onderstaande formule voor veelvlakken:

$$
    H - R + Z = 2
$$

waarbij $$H$$ het aantal hoekpunten, $$R$$ het aantal ribben en $$Z$$ het aantal vlakken voorstelt.

Elk veelvlak moet voldoen aan deze vergelijking. Met behulp van deze vergelijk is het ook mogelijk om aan te tonen dat er slechts vijf platonische lichamen of <a href="https://nl.wikipedia.org/wiki/Regelmatig_veelvlak" target="_blank">regelmatige veelvlakken</a> bestaan.

![De 5 platonische lichamen.](media/platonic.png "Foto door Drummyfish op Wikimedia."){:data-caption="De 5 platonische lichamen." width="40%"}


## Opgave
Schrijf een functie `euler_formule( h, r, z )` die voor de gegeven parameters controleert of dit een veelvlak kan voorstellen. Indien ja wordt `True` op het scherm afgedrukt, indien niet `False`.

#### Voorbeeld
Een kubus heeft bijvoorbeeld 8 hoekpunten, 12 ribben en 6 vlakken, zodat:
```
>>> euler_formule( 8, 12, 6 )
True
```
Een <a href="https://nl.wikipedia.org/wiki/Grote_dodeca%C3%ABder" target="_blank">grote dodocaëder</a> is geen veelvlak:
```
>>> euler_formule( 12, 30, 12 )
False
```