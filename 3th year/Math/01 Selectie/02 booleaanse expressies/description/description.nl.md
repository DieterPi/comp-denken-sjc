## Booleaanse expressies
De test die bepaalt of een tak van een keuzestructuur wordt uitgevoerd noemt men een **booleaanse expressie**. De acties worden enkel uitgevoerd indien de test `waar` of `True` is.

#### Vergelijkingen

De meestgebruikte booleaanse expressies zijn vergelijkingen. Een vergelijking bestaat uit twee waardes met een **vergelijkingsoperator** ertussen:

| operator | beschrijving |
|:--------:|-------------|
|        `<`  |    kleiner dan |
|        `<=` |  kleiner dan of gelijk aan |
|        `==`  | gelijk aan |
|        `>=` |  groter dan of gelijk aan |
|        `>`  |  groter dan |
|        `!=` |  niet gelijk aan |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

{: .callout.callout-danger}
> #### Opgelet
> Een veel gemaakte fout is om twee waarden te vergelijken met een enkele `=`. Dit is echter de toekenningsoperator. Probeer bijvoorbeeld eens onderstaande code uit:

```python
x = 46
if x % 10 = 6:
    print( 'x heeft een 6 als eenheid' )
```

Je kan deze booleaanse expressies ook toekennen aan een variabele. 

```python
getal = int( input( 'Geef een getal in: ' ) )
is_even = getal % 2 == 0
print( is_even )
```

#### Logische operatoren
Met behulp van de logische operatoren `and`, `or` en `not` kan je booleaanse expressies combineren. In Minecraft deed je dit als volgt:
![minecraft logische operator](media/logische_en.png "minecraft logische operator"){:data-caption="Een logische operator in Minecraft Education Edition" width="218px"}

In Python gebruik je de volgende code:
```python
t = True
f = False
print( t and t )
print( t and f )
print( f and t )
print( f and f )
print( t or t )
print( t or f )
print( f or t )
print( f or f )
print( not t )
print( not f )
```

Kijk wel uit bij het gebruik van logische operatoren, combinaties kunnen snel leiden tot onverwachte resultaten. Gebruik daarom haakjes om ervoor te zorgen dat ze in de juiste volgorde geëvalueerd worden.

Geef voor de code hieronder waardes voor `a`, `b`, and `c`, die ertoe leiden dat de twee expressies verschillende uitkomsten hebben.

```Python
a = # True of False?
b = # True of False?
c = # True of False?

print( (a and b) or c )
print( a and (b or c) )
```

## Opgave
Schrijf een programma dat een (komma)getal inleest. Is het getal positief dan verschijnt de tekst `positief`. In het andere geval verschijnt `strikt negatief`.