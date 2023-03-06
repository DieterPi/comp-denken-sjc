## Opgave
Naast het gewone, rekenkundige, gemiddelde zijn er ook andere manieren om een gemiddelde van getallen te berekenen. Eén van deze methodes is het zogenaamde *harmonisch* gemiddelde. Het harmonisch gemiddelde x<span style="vertical-align:sub;">h</span> van de reële getallen a en b is gedefinieerd als:

$$
    x_h = \dfrac{2}{\frac{1}{a}+\frac{1}{b}}
$$

Schrijf een functie `harmonisch_gemiddelde( a, b )` die het harmonisch gemiddelde berekent en deze waarde afdrukt. Rond af op 2 cijfers.

#### Voorbeelden
```
>>> harmonisch_gemiddelde( 100, 120 )
109.09
```
```
>>> harmonisch_gemiddelde( 128, 26 )
43.22
```