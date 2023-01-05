Een alternatieve methode om de vierkantswortel te berekenen werd beschreven in het <a href="https://en.wikipedia.org/wiki/Bakhshali_manuscript" target="_blanc">Bakshali manuscript</a>. Vernoemd naar het dorp waar dit manuscript werd gevonden, tegenwoordig in Pakistan.

Deze methode werkt een analoge manier. Stel dat we de vierkantswortel willen berekenen van een natuurlijk getal s.

- We starten met een initiële schatting van s, en noemen die x<span style="vertical-align:sub;">0</span>. 
- Daarna bereken we in elke stap een meer nauwkeurige benadering van de vierkantswortel op basis van de volgende formule, waar telkens hulpvariabelen a<span style="vertical-align:sub;">n</span> en b<span style="vertical-align:sub;">n</span> berekend worden:

$$
a_n = \dfrac{s - x_n^2}{2\cdot x_n},\qquad b_n = x_n + a_n, \qquad\qquad x_{n+1} = b_n - \dfrac{a_n^2}{2\cdot b_n}
$$

Laten we dit algoritme bijvoorbeeld eens toepassen voor de berekening van $$\sqrt{17}$$. We kiezen $$x_0=6$$ als een initiële schatting voor $$\sqrt{17}$$. In een volgende stap bekomen we de volgende meer nauwkeurige benadering van de vierkantswortel: 

$$
a_0 = \dfrac{17-6^2}{12}, \qquad b_0 = 6 + a_0, \qquad\qquad x_1 = b_0 - \dfrac{a_0^2}{2\cdot b_0} = 4,132861635\ldots
$$

Daarna moeten we deze procedure gewoon blijven herhalen om de benadering te verbeteren.

$$
a_1 = \dfrac{17-x_1}{2\cdot x_1}, \qquad b_1 = x_1 + a_1, \qquad\qquad x_2 = b_1 - \dfrac{a_1^2}{2\cdot b_1}= 4,123105626\ldots
$$

## Opgave

Schrijf een functie `bakshali_methode()` met twee getallen als parameter, het eerste is het **grondtal** van de wortel s, het tweede de **initiële schatting** x<span style="vertical-align:sub;">0</span>. Laat de methode stoppen indien de verbetering kleiner is dan 10<span style="vertical-align:super;">-12</span> (`pow( 10, -12 )`).

Druk ook telkens de stap en de benaderde waarde af.

#### Voorbeelden
De uitvoer voor grondtal 17 en startwaarde 6 is:
```
>>> bakshali_methode( 17, 6 ) 
0 : 6
1 : 4.132861635220126
2 : 4.12310562563374
3 : 4.123105625617661
```