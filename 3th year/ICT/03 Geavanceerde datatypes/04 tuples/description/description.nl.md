## Tupels
Een tupel is ook een **geordend** datatype dat meerdere elementen kan bevatten van een ander datatype. Dit datatype wordt gedefinieerd met behulp van `( )` en kommas tussen de elementen. Via `len()` bepaal je de lengte van de tupel. 

```python
tupel = ( -5, 6, 8 )
print( tupel )
print( type( tupel ) )
print( len( tupel ) )
```
Hier zie je een lijst met drie elementen, telkens van het datatype `int`. Je kan opnieuw de elementen apart raadplegen met behulp van de rangnummers.
```python
tupel = ( -5, 6, 8 )
print( tupel[1] )
```

### Lijsten of tupels?
Het grote verschil met lijsten is dat je geen elementen apart kan gaan bewerken.
```python
lijst = [ -5, 6, 8 ]
lijst[1] = 7
print( lijst )
```

```python
tupel = ( -5, 6, 8 )
tupel[1] = 7
print( tupel )
```

Je kan aan een tupel dus ook geen waarden toevoegen via `append()` of verwijderen via `remove()`. Tupels worden vooral gebruikt om met coördinaten te werken.
```python
A = ( 1, 3)
print( 'Punt A heeft x-coördinaat', A[0], 'en y-coördinaat', A[1] )
```

## Opgave
De (Euclidische) afstand $$d$$ van de oorsprong tot een punt $$P(x,y)$$ wordt gegeven door de volgende formule:

$$
    d = \sqrt{x^2+y^2}
$$

Schrijf een functie `afstand( coordinaat )` die de afstand van een bepaalde coördinaat tot de oorsprong berekent en deze waarde **retourneert**. Rond af op 2 cijfers.

#### Voorbeeld
```
>>> afstand( (3,4) )
5
```