## Lijsten
Een lijst is een **geordend** datatype dat meerdere elementen kan bevatten van een ander datatype. Lijsten worden gedefinieerd met vierkante haakjes `[  ]` en kommas tussen de elementen. Via `len()` bepaal je de lengte van de lijst.

```python
lijst = [ 'banaan', 'appel', 'peer' ]
print( lijst )
print( type( lijst ) )
print( len( lijst ) )
```
Hier zie je een lijst met drie elementen, telkens van het datatype `string`. Je kan gemakkelijk de elementen van deze lijst apart bewerken, dat doe je met behulp van de rangnummers. In Minecraft zou je als volgt werken:

![minecraft](media/minecraft.png "minecraft"){:data-caption="Een lijst gebruiken in Minecraft Education Edition" width="600px"}

```python
lijst = [ 'banaan', 'appel', 'peer' ]
print( lijst[0] )
print( lijst[1] )
print( lijst[2] )
```

{: .callout.callout-danger}
> #### Opgelet
> Merk op dat het **eerste** element van de lijst rangnummer `0` heeft!

### Methodes
Met behulp van `.append()` kan je nieuwe items aan een lijst toevoegen.
```python
lijst = [ 'banaan', 'appel', 'peer' ]
lijst.append( 'mango' )
print( lijst )
```

Met behulp van `.pop()` kan je een item uit een lijst verwijderen.
```python
lijst = [ 'banaan', 'appel', 'peer' ]
lijst.pop( 1 )
print( lijst )
```

Met behulp van `.extend()` kan je verschillende lijsten samenvoegen.
```python
lijst = [ 'banaan', 'appel', 'peer' ]
lijst_exotisch = [ 'mango', 'ananas' ]
lijst.extend( lijst_exotisch )
print( lijst )
```

Met behulp van `.sort()` kan je een lijst sorteren. Lijsten met tekst worden alfabetisch gesorteerd, numerieke lijsten worden van laag naar hoog gesorteerd.
Door `reverse = True` toe te voegen als argument wordt de volgorde omgedraaid.
```python
lijst = [ 'banaan', 'appel', 'peer' ]
lijst.sort()
print( lijst )
lijst.sort( reverse = True )
print( lijst )
```

Met behulp van `.count()` kan je tellen hoe vaak een element in een lijst voorkomt.
```python
lijst = [ 'banaan', 'appel', 'peer', 'banaan', 'druif', 'kers' ]
print( lijst.count( 'banaan' ) )
```

## Opgave
Beschouw onderstaande lijst van jongensnamen. Schrijf een programma dat drie keer naam vraagt en vervolgens telt hoeveel keer de naam voorkomt.
De uiteindelijke score is de **som** van al deze aantallen.

#### Voorbeeld
Voor de achtereenvolgense invoer `Louis`, `Jarre`, `Bram` verschijnt:
```
8
```