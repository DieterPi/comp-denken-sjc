Onderstaande twee **ongerichte** grafen zijn identiek, ondanks dat de verzameling van de bogen niet gelijk is. De volgorde waarin de boven worden opgelijst maakt immers niet uit. Gezien de graaf ongericht is, maakt ook de volgorde van de knopen niet uit.

```python
# Graaf 1
V = ['A', 'B', 'C', 'D', 'E']
E = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'D'), ('D', 'B'), ('B', 'E')]
```

```python
# Graaf 2
V = ['A', 'B', 'C', 'D', 'E']
E = [('E', 'B'), ('C', 'A'), ('B', 'A'), ('D', 'B'), ('C', 'D'), ('B', 'C')]
```

## Opgave

Schrijf een functie `identiek( E1, E2 )` die gegeven twee lijsten met bogen controleert of deze grafen aan elkaar gelijk zijn.

#### Voorbeeld
```
>>> identiek( [('A', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'D'), ('D', 'B'), ('B', 'E')],
              [('E', 'B'), ('C', 'A'), ('B', 'A'), ('D', 'B'), ('C', 'D'), ('B', 'C')] )
True
```
