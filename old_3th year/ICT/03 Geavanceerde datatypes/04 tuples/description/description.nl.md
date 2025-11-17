## Tupels
Een tupel is ook een **geordend** datatype dat meerdere elementen kan bevatten van een ander datatype. Dit datatype wordt gedefinieerd met behulp van `( )` en kommas tussen de elementen. Via `len()` bepaal je de lengte van de tupel. 

```python
tupel = ( -5, 6, 8 )
print( tupel )
print( type( tupel ) )
print( len( tupel ) )
```

Hier zie je een lijst met drie elementen, telkens van het datatype `int`. Je kan de elementen apart raadplegen met behulp van de rangnummers. **Deze rangnummers beginnen echter vanaf 0!**
```python
tupel = ( -5, 6, 8 )
print( tupel[0] )
print( tupel[1] )
print( tupel[2] )
```

Tupels worden vooral gebruikt om met coördinaten te werken.

```python
A = ( 1, 3)
print( 'Punt A heeft x-coördinaat', A[0], 'en y-coördinaat', A[1] )
```

## Opgave
De (Euclidische) afstand $$d$$ van de oorsprong tot een punt $$P(x,y)$$ wordt gegeven door de volgende formule:

$$
    d = \sqrt{x^2+y^2}
$$

Schrijf een functie `afstand( coordinaat )` die de afstand van een bepaalde coördinaat tot de oorsprong berekent en deze waarde op het scherm afdrukt. Rond af op 2 cijfers.

#### Voorbeeld
```
>>> afstand( (3,4) )
5
```