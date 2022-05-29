Uit onderzoek blijkt dat 70% van de Fransen onvoldoende informatie hebben over de impact van hetgeen ze eten op het milieu. Daarom ontwikkelde men de Eco-Score, een labelsysteem dat op basis van verschillende kenmerken (zoals verpakking, transport, hoeveelheid waterverbruik, enz...) een ecologische score toekent aan het voedingsmiddel.

Zo krijgt de pizza 'Ristorante Pizza quattro formaggi' van Dr. Oetker volgens <a href='https://nl.openfoodfacts.org/product/4001724818908/ristorante-pizza-quattro-formaggi-dr-oetker' target='_blank'>openfoodfacts.org</a> de volgende Eco-score.

![Eco-Score](media/ecoscore.png "Eco-Score"){:data-caption="Eco-Score van een Dr. Oetker pizza" width="250px"}

De letter in het Eco-Scorelogo is vastgesteld door middel van uitgebreide berekeningen. De basis is een zogenaamde levenscyclusanalyse (LCA). Uit de LCA volgt een score van 0 tot 100. Elke 20 punten lager betekent een twee keer zo hoge milieu-impact. 

| punten | letter | betekenis |
|:--------:|-------------|-----|
| ≤ 20 | E | Erg hoge milieu-impact |
| > 20 en ≤ 40 | D |
| > 40 en ≤ 60 | C |
| > 60 en ≤ 80 | B |
| > 80 en ≤ 100 | A | Erg lage milieu-impact |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

## Opgave
Schrijf een functie `ecoscore()` met de score uit de LCA als parameter waarbij het programma de letter uit de Eco-Score op het scherm weergeeft.

#### Voorbeeld
```
>>> ecoscore( 56 )
C
>>> ecoscore( 88 )
A
```