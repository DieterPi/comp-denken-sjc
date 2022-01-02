## Functies
In de vorige hoofdstukken heb je al verschillende functies gebruikt. Denk maar aan de in- en uitvoer functies `input()` en `print()`. In dit onderdeel ga je zelf functies schrijven. Waarom zou je zelf functies willen schrijven?

-   Er is een bepaalde functionaliteit die je op **meerdere** plekken in je programma nodig hebt, dan kan je die beter in een aparte functie stoppen in plaats van de code telkens te kopiëren.

-   Door functies met parameters te schrijven zal de code duidelijker worden, gemakkelijker te lezen en te onderhouden.

-   Je programma is te lang om de inhoud goed te blijven overzien. Door de code op te splitsen in functies blijf je veel langer grip houden op de inhoud en werking.

-   ...

#### Definitie
```python
def <functienaam>( <parameter_lijst>) :
    <acties>
```
Hieronder zie je een voorbeeld van een functie. Je merkt meteen op dat dit veel gemakkelijker leest dan de code `print( 'Hallo', naam, '!')` 4 keer te herhalen. Niet enkel leest het eenvoudiger, maar indien de tekst zou willen wijzigen naar `'Goeiedag', naam,'!'`, dan hoef je dit maar op één plaats te wijzigen.

```python
def hallo( naam ):
    print( 'Hallo', naam, '!')

hallo( 'Jan' )
hallo( 'Piet' )
hallo( 'Joris' )
hallo( 'Korneel' )
```

Je kan eenvoudig een functie met meerdere argumenten aanmaken, bijvoorbeeld:

```python
def vermenigvuldig( x, y ):
    resultaat = x * y
    print( resultaat )

vermenigvuldig( 2020 , 5278238 )
vermenigvuldig( 2, 3 )
```


## Opgave
Beschouw onderstaande code, deze bevat een kleine **fout**. Corrigeer deze code zodat de oppervlakte van een driehoek met basis 4.5 en hoogte 1 wordt weergegeven op het scherm.