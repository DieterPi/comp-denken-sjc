Python kan heel wat bewerkingen toepassen op tekst. Probeer bijvoorbeeld het onderstaande uit:

```python
tekst = 'ha'
print( 3 * tekst )
```
Je kan ook tekst *optellen*, of **concateneren**:

```python
begin = '>'
einde = '<'
print( 3 * begin + ' Welkom ' + 3 * einde )
```

Daarnaast bezit Python over heel wat **functies** om tekstfragmenten te bewerken. Wat doet het onderstaande?

```python
tekst = 'Pif, Poef, Paf'
print( len( tekst ) )
print( tekst[0] )
print( tekst[-1] )
print( tekst[0:3] )
print( tekst[5:9] )
print( tekst[:-5] )
```

Men noemt het getal tussen de vierkante haakjes de **index** van de karakters. Het eerste karakter heeft index 0, je haalt dit karakter op via `tekst[0]`. Wat haalt een negatieve index op?

Je kan Python binnen tekst laten zoeken met de `find()` functie. De output van de functie is de index van het eerste karakter dat overeenkomt met het gezochte.

```python
tekst = 'Hallo'
print( tekst.find( 'a' ) )
print( tekst.find( 'll' ) )
print( tekst.find( 'L' ) )
```

Wat is de ouput indien een karakter niet terug wordt gevonden?

Je kan ook de functie `count()` toepassen op een regel tekst.
```python
tekst = 'Abracadabra'
print( tekst.count( 'a' ) )
print( tekst.count( 'b' ) )
```

## Opgave

Schrijf een programma dat een tekstinvoer vraagt van woorden gescheiden door spaties. Schrijf een programma dat bepaalt uit hoeveel woorden het de tekstinvoer bestaat.

#### Voorbeeld
De invoer `Hello world` resulteert in de uitvoer:
```
2
```

De invoer `Dit is een oefening` resulteert in:
```
4
```