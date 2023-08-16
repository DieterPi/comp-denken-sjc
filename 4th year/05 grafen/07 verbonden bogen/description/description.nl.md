## Opgave

Schrijf een functie `verbonden_bogen( v, E )` die gegeven een knoop `v` en een **lijst** `E` met (gewogen) bogen alle bogen bepaalt die met `v` verbonden zijn.

#### Voorbeeld

![De bogen verbonden met C in een gewogen graaf.](media/connected.png "De bogen verbonden met C in een gewogen graaf."){:data-caption="De bogen verbonden met C in een gewogen graaf." .light-only width="30%"}

![De bogen verbonden met C in een gewogen graaf.](media/connected_dark.png "De bogen verbonden met C in een gewogen graaf."){:data-caption="De bogen verbonden met C in een gewogen graaf." .dark-only width="30%"}


```
>>> verbonden_bogen( 'C', [('A', 'B', 3), ('B', 'C', 2), ('C', 'A', 5), ('C', 'D', 2), ('D', 'B', 8), ('B', 'E', 3)] )
[('B', 'C', 2), ('C', 'A', 5), ('C', 'D', 2)]
```
