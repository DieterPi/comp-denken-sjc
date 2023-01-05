## Opgave
Naast het gewone, rekenkundige, gemiddelde zijn er ook andere manieren om een gemiddelde van getallen te berekenen. Eén van deze methodes is het zogenaamde *harmonisch* gemiddelde. Het harmonisch gemiddelde $$x_h$$ van de reële getallen $$a$$ en $$b$$ is gedefinieerd als:

$$
x_h = \dfrac{2}{\frac{1}{a}+\frac{1}{b}}
$$

Schrijf een functie `harmonisch_gemiddelde( a, b )` die het harmonisch gemiddelde berekent en deze waarde **retourneert**. Rond af op 2 cijfers.

{: .callout.callout-warning}
> #### Verduidelijking
> Het is niet de bedoeling dat je een functie schrijft die de waarde *afdrukt*, enkel *retourneert* (met behulp van `return`). Om te testen kan je de waarde natuurlijk wel afdrukken.

#### Voorbeelden
```
>>> harmonisch_gemiddelde( 100, 120 )
109.09
```
```
>>> harmonisch_gemiddelde( 128, 26 )
43.22
```