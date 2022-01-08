<div style="text-align: right"><i class="mdi mdi-18 mdi-star"></i><i class="mdi mdi-18 mdi-star"></i><i class="mdi mdi-18 mdi-star-outline"></i><i class="mdi mdi-18 mdi-star-outline"></i></div>

Het algoritme van **Prim**.

## Opgave

Schrijf een functie `MST_prim( V, E )` waarbij `V` een lijst met toppen voorstelt en `E` een lijst opgesteld uit tupels van bogen en hun gewicht.

#### Voorbeelden
```
>>> MST_prim( ['A','B','C','D','E'], 
              [('A','B',3), ('B','C',4),('C','D',2),('B','D',7),('B','E',8)] )
[('A', 'B', 3), ('B', 'C', 4), ('C', 'D', 2), ('B', 'E', 8)]
>>> MST_prim( ['A', 'B', 'C', 'D', 'E'], 
              [('A', 'E', 3), ('C', 'D', 10), ('C', 'A', 5), ('D', 'E', 2), ('A', 'D', 15), ('C', 'E', 11), ('E', 'B', 6)] )
[('A', 'E', 3), ('D', 'E', 2), ('C', 'A', 5), ('E', 'B', 6)]
```