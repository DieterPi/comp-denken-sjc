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

Men noemt het getal tussen de vierkante haakjes de **index** van de karakters. Het eerste karakter heeft index 0, je haalt dit karakter op via `tekst[0]`.

Je kan Python binnen tekst laten zoeken met de `find()` functie. De output van de functie is de index van het eerste karakter dat overeenkomt met het gezochte.

```python
tekst = 'Hallo'
print( tekst.find( 'e' ) )
print( tekst.find( 'll' ) )
print( tekst.find( 'L' ) )
```

Wat is de ouput indien een karakter niet terug wordt gevonden?

Je kan ook de functie `count()` toepassen op een regel tekst.
```python
tekst = 'Abracadabra'
print( tekst.count( 'a' ) )
print( tekst.find( 'b' ) )
```



## Opgave

Schrijf een programma dat aan een gebruik een aantal uur $$U$$, minuten $$M$$ en seconden $$S$$ sinds middernacht vraagt (met $$0 \leqslant H \leqslant 12, 0 \leqslant M \leqslant 60$$ en $$0\leqslant S \leqslant 60$$).

Vervolgens berekent het programma de hoek (in **graden**) die de uurwijzer op de klok aangeeft. Rond het resultaat af op 5 cijfers na de komma.

#### Voorbeeld
Na exact 3 uur maakt de uurwijzer een hoek van 90°
```
90.0 graden
```

Na 1 uur en 2 minuten en 6 seconden maakt de uurwijzer een hoek van 31.05 graden.
```
31.05 graden
```