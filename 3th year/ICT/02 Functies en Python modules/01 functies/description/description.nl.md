## Functies
In de vorige hoofdstukken heb je al verschillende functies gebruikt. Denk maar aan de in- en uitvoer functies `input()` en `print()`. In dit onderdeel ga je zelf functies schrijven. Waarom zou je zelf functies willen schrijven?

-   Er is een bepaalde functionaliteit die je op **meerdere** plekken in je programma nodig hebt, dan kan je die beter in een aparte functie stoppen in plaats van de code telkens te kopiëren.

-   Door functies met parameters te schrijven zal de code duidelijker worden, **gemakkelijker te lezen** en te **onderhouden**.

-   Je programma is te lang om de inhoud goed te blijven overzien. Door de code op te splitsen in functies blijf je veel langer grip houden op de inhoud en werking.

-   ...

### Definitie
```python
def <functienaam>( <parameter_lijst>) :
    <acties>
```

{: .callout.callout-danger}
> #### Opgelet
> Zeer belangrijk in het aanmaken van een functie is de **indentatie**. Je merkt dat de acties in de functie naar rechts werden *opgeschoven* of *geïndenteerd*. Dat doe je gemakkelijk met behulp van de **tab** toets.

Hieronder zie je een voorbeeld van een functie. Je merkt meteen op dat dit veel gemakkelijker leest dan de code `print( 'Hallo', naam, '!')` 4 keer te herhalen. Niet enkel leest het eenvoudiger, maar indien de tekst zou willen wijzigen naar `'Goeiedag', naam,'!'`, dan hoef je dit maar op één plaats te wijzigen.

```python
def hallo( naam ):
    print( 'Hallo', naam, '!')

hallo( 'Jan' )
hallo( 'Piet' )
hallo( 'Joris' )
hallo( 'Korneel' )
```

Je kan eenvoudig een functie met meerdere **parameters** aanmaken, bijvoorbeeld:

```python
def vermenigvuldig( x, y ):
    resultaat = x * y
    print( resultaat )

vermenigvuldig( 2020 , 5278238 )
vermenigvuldig( 2, 3 )
```

### return
Parameters worden gebruikt om informatie van buiten de functie naar de functie toe te communiceren. Vaak wil je ook informatie vanuit de functie naar het programma buiten de functie toe communiceren. Daartoe dient het commando `return`.

In de vorige functies werd de uiteindelijke uitkomst gewoon afgedrukt, maar wat als je ermee zou willen verder rekenen?

Uit de wetten van Newton volgt de volgende formule voor de valafstand $$d$$ van een object gedurende een tijd $$t$$. Op aarde is de zwaarteveldsterkte $$g = 9.81 \frac{\text{m}}{\text{s}^2}$$

$$
d = \dfrac{1}{2}\cdot g \cdot t^2
$$

We kunnen de valafstand eenvoudig berekenen met behulp van een functie in Python. 
```python
def valafstand( t, g = 9.81 ):
    d = 1/2 * g * pow( t, 2 )
    return d

print( valafstand( 3 ) )
print( valafstand( 4 ) > 88 )
```
Zoals je in de laatste regel kan zien zorgt `return` ervoor dat je gemakkelijk kan controleren of een object na 4 seconden meer dan 88 meter heeft afgelegd. We kunnen verder *rekenen* met de *uitvoer* van deze functie.

De toevoeging `g = 9.81` bij de parameter zorgde ervoor dat $$g$$ **standaard** de waarde $$9.81$$ krijgt. Op de maan is dit slechts $$1,625 \frac{\text{m}}{\text{s}^2}$$ wat nu gemakkelijk te berekenen valt. $$g$$ was bij deze functie dus een *optionele* parameter.
```python
print( valafstand( 3, 1.625 ) )
print( valafstand( 4, 1.625) > 88 )
```

#### return of print?
Heel belangrijk is het verschil tussen `print` en `return`. Beschouw de volgende stukjes code:
```python
def plus3( a ):
    print( a+3 )
plus3( 5 )
```

```python
def plus3( a ):
    return a+3 
print( plus3( 5 ) )
```
Beide stukjes code resulteren tot het printen van de waarde 8. Toch zijn de functies **fundamenteel** verschillend!

## Opgave
Beschouw onderstaande code, deze bevat een kleine **fout**. 

Corrigeer deze code zodat als uitvoer verschijnt `Een driehoek met basis 4.5 en hoogte 1.0 heeft oppervlakte 2.25`.