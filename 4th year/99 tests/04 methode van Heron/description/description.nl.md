Sommige vierkantswortels zoals $$\sqrt{25}$$ of $$\sqrt{144}$$ kennen we van buiten, maar hoe berekenen we $$\sqrt{17}$$ bijvoorbeeld? Tegenwoordig grijp je dan meteen naar een rekentoestel, maar hoe deed men dit vroeger, toen er nog geen rekentoestellen of computers bestonden?

De methode van Heron is wellicht het oudste algoritme voor de berekening van $$\sqrt{s}$$ met $$s\in \mathbb{N}$$. Ze werd vernoemd naar de Griekse wiskundige <a href="https://nl.wikipedia.org/wiki/Heron_van_Alexandri%C3%AB" target="_blanc">Heron van Alexandrië</a> die ruim 2000 jaar geleden de eerste expliciete beschrijving gaf van een methode voor het berekenen van de vierkantswortel van een willekeurig getal. Deze methode is ook gekend als de Babylonische methode — een verwijzing naar de Babyloniërs die ons de oudste gekende wiskundeteksten achterlieten. 

![Heron van Alexandrië.](media/Heron_Alexandrie.jpg "Heron van Alexandrië volgens de Codex van st Gregory Nazianzenos, een Grieks manuscript uit de 9e eeuw."){:data-caption="Heron van Alexandrië." width="30%"}

Deze methode werkt op de volgende manier. Stel dat we de vierkantswortel willen berekenen van een natuurlijk getal $$s$$. 

- We starten met een initiële schatting van $$s$$, en noemen die $$x_0$$. 
- Daarna bereken we in elke stap een meer nauwkeurige benadering van de vierkantswortel op basis van de volgende formule:

$$
x_{n+1} = \dfrac{1}{2}\left(x_n+\dfrac{s}{x_n}\right)
$$

Laten we dit algoritme bijvoorbeeld eens toepassen voor de berekening van $$\sqrt{17}$$. We kiezen $$x_0=6$$ als een initiële schatting voor $$\sqrt{17}$$. In een volgende stap bekomen we de volgende meer nauwkeurige benadering van de vierkantswortel: 

$$
x_1 = \dfrac{1}{2}\left( 6+\dfrac{17}{6}\right) = 4,416666666\ldots
$$

Daarna moeten we deze procedure gewoon blijven herhalen om de benadering te verbeteren.

$$
x_2 = \dfrac{1}{2}\left( x_1 + \dfrac{17}{x_1}\right) = 4.132861635\ldots
$$

## Opgave

Schrijf een functie `babylonische_methode()` met twee getallen als parameter, het eerste is het **grondtal** van de wortel s, het tweede de **initiële schatting** x<span style="vertical-align:sub;">0</span>. Laat de methode stoppen indien de verbetering kleiner is dan 10<span style="vertical-align:super;">-15</span>.

Druk ook telkens de stap en de benaderde waarde af.

#### Voorbeelden
De uitvoer voor grondtal 17 en startwaarde 6 is:
```
>>> babylonische_methode( 17, 6 ) 
0 : 6
1 : 4.416666666666667
2 : 4.1328616352201255
3 : 4.12311714060797
4 : 4.12310562563374
5 : 4.123105625617661
```