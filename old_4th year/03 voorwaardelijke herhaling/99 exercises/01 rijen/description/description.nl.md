Een **rekenkundige rij** is een rij waarbij het **verschil** tussen elke opeenvolgende waarde constant is. Indien de startwaarde bijvoorbeeld 5 is en het verschil 2, dan ziet de rij er als volgt uit:

$$
    5,\qquad 7,\qquad 9,\qquad 11,\qquad 13,\ldots
$$

Het volgende programma zal voor een bepaalde startwaarde en verschil zoeken naar het rangnummer waarbij de **som van alle termen** kleiner is dan 100:

```python
a = int( input( 'Geef de startwaarde in:' ) )
v = int( input( 'Geef het verschil in:' ) )

term = a
som = a
i = 1
while som < 100:
    print( i, ':', som )
    term += v
    som += term
    i += 1
```

## Opgave

Een **meetkundige rij** is een rij waarbij het **quotiënt** tussen elke opeenvolgende waarde constant is. Is de startwaarde bijvoorbeeld 5 en het quotiënt 2, dan ziet de rij er als volgt uit:

$$
    5,\qquad 10,\qquad 20,\qquad 40,\qquad 80,\ldots
$$

Pas nu het bovenstaande programma aan zodat voor een bepaalde **reële** startwaarde en **reële** quotiënt het rangnummer bepaald wordt zodat de som van alle termen kleiner is dan 500. Druk de som telkens af met 2 cijfers na de komma.

#### Voorbeelden
Invoer van startwaarde `5.0` en quotiënt `2.0` leidt tot:
```
1 : 5.0
2 : 15.0
3 : 35.0
4 : 75.0
5 : 155.0
6 : 315.0
```

Invoer van startwaarde `102.0` en quotiënt `1.1` leidt tot:
```
1 : 102.0
2 : 214.2
3 : 337.62
4 : 473.38
```

