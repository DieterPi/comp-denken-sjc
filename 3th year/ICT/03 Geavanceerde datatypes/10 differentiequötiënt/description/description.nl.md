Als $$A(x_1,y_1)$$ en $$B(x_2,y_2)$$ twee punten (met $$x_1 \not = x_2$$) zijn van de grafiek van een functie dan berekent men het differentiequötiënt op dat interval als volgt:

$$
\dfrac{\delta y}{\Delta x} = \dfrac{y_2-y_1}{x_2-x_1}
$$

## Opgave
Schrijf een functie `differentiequotient( koppel1, koppel2 )` die gegeven 2 tupels het differentiequötiënt berekent en afdrukt. Rond af op 2 cijfers na de komma.

#### Voorbeeld
```
>>> differentiequotient( (1,3), (5,4) )
(205, 224, 40)
(40, 205, 224)
```