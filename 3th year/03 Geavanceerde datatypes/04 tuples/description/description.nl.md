## Tuples
Een tuple is ook een **geordend** datatype dat meerdere elementen kan bevatten van een ander datatype. Dit datatype wordt gedefinieerd met behulp van `( )` en kommas tussen de elementen. Via `len()` bepaal je de lengte van de tuple. 

```python
tuple = ( -5, 6, 8 )
print( tuple )
print( len( tuple ) )
```
Hier zie je een lijst met drie elementen, telkens van het datatype `int`. Je kan opnieuw de elementen apart raadplegen met behulp van de rangnummers.
```python
tuple = ( -5, 6, 8 )
print( lijst[1] )
```

### Lijsten of tuples?
Het grote verschil met lijsten is dat je geen elementen apart kan gaan bewerken.
```python
lijst = [ -5, 6, 8 ]
lijst[1] = 7
print( lijst )
```

```python
tuple = ( -5, 6, 8 )
tuple[1] = 7
print( tuple )
```

Je kan aan een tuple dus ook geen waarden toevoegen via `append()` of verwijderen via `remove()`. Tuples worden vooral gebruikt om met coördinaten te werken.
```python
A = ( 1, 3)
print( 'Punt A heeft x-coördinaat', A[0], 'en y-coördinaat', A[1] )
```

## Opgave
De afstand $$d$$ van de oorsprong tot een punt $$P(x,y)$$ wordt gegeven door de volgende formule:

$$
    d = \sqrt{x^2+y^2}
$$

Schrijf een functie `afstand( coordinaat )` die de afstand van een bepaalde coördinaat tot de oorsprong berekent en deze waarde **retourneert**. Rond af op 2 cijfers.

#### Voorbeeld
De afstand van `(3,4)` tot de oorsprong is `5`.