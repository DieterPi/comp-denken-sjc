Als $$A(x_1,y_1)$$ en $$B(x_2,y_2)$$ (met $$x_1 \not = x_2$$) twee punten zijn van de grafiek van een functie dan berekent men het differentiequötiënt op dat interval als volgt:

$$
\dfrac{\Delta y}{\Delta x} = \dfrac{y_2-y_1}{x_2-x_1}
$$

## Opgave
Schrijf een functie `differentiequotient( koppel1, koppel2 )` die gegeven 2 tupels het differentiequötiënt berekent en afdrukt. Rond af op 2 cijfers na de komma.
Zorg dat het programma overweg kan met bijzondere invoer.

#### Voorbeelden
```
>>> differentiequotient( (1,3), (5,4) )
Het differentiequötiënt op het interval [ 1 , 5 ] is: 0.25
```
```
>>> differentiequotient( (5,3), (5,4) )
Deze twee punten hebben eenzelfde x coördinaat, hier kan je dus geen differentiequötiënt berekenen
```

{: .callout.callout-info}
> #### Tip
> Je kan uit een *tupel* met lengte 2 de aparte elementen halen via `tupel[0]` en `tupel[1]`.