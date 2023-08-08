## Opgave
Schrijf een programma dat een schaakbordpatroon afdrukt. Implementeer een functie `schaakbord( r, k)`.

Hierbij stelt:
    `r`, het aantal rijen en
    `k`, het aantal kolommen
voor

(Het teken linksboven moet `x` zijn.)

Gebruik in deze oefening de optie `end` bij een printopdracht. Beschouw bijvoorbeeld:
```python
print('x', end = ' ')
print('.', end = ' ')
print() # dit print een nieuwe regel
print('x', end = ' ')
print('.', end = ' ')
print('x', end = ' ')
print('.', end = ' ')
```

#### Voorbeeld
```
>>> schaakbord( 6, 8 )
 x . x . x . x . 
 . x . x . x . x 
 x . x . x . x . 
 . x . x . x . x 
 x . x . x . x . 
 . x . x . x . x 
```