## Basisfuncties
Functies vormen een essentieel onderdeel van het programmeren. Je hebt in de vorige lessen al enkele basisfuncties gebruikt. Zo geeft de functie `print()` iets weer op het scherm. De functie `type()` bepaalt dan weer een datatype.

Later zullen we zelf eigen functies gaan samenstellen, maar eerst zal het handig zijn om kennis te maken met enkele functies die Python reeds voor ons klaar heeft.

### Functies en argumenten
De functie `print()` accepteert meerdere **argumenten**, probeer bijvoorbeeld de volgende code uit:

```python
pi = 3.14159
print( 'Het getal pi is afgerond op 5 cijfers:', pi )
```

De functie `type()` aanvaardt slechts één argument, het argument waarvan je het datatype wil bepalen. Probeer bijvoorbeeld eens de volgende code uit:
```python
x = 5
y = 1.5
print( type( x, y ) )
```

### Andere basisfuncties
Een zeer handige functie is `input()`. Met behulp van die functie kan je de gebruiker om een invoer vragen. Test het meteen eens uit via:
```python
x = float(input( 'Geef een getal in: ' ))
print( 'Het dubbele van', x, 'is', 2*x )
```
Controleer wat er gebeurt indien je `float()` weglaat.

Andere handige functies zijn `abs()`, `min()` en `max()`, `pow()` en `round()`. Beoordeel zelf wat het nut van deze functies in met behulp van het vorige voorbeeld.

```python
x = -2
y = 3
z = 1.27

print( 'abs( x ):', abs( x ) )
print( 'max( x, y, z ):', max( x, y, z ) )
print( 'min( x, y, z):', min( x, y, z ) )
print( 'pow( x, y) ):', pow( x, y ) )
print( 'round( z, 1 ):', round( z, 1 ) )
```

## Opgave
Schrijf een programma dat drie **gehele** getallen vraagt en dan het maximum, minimum en het gemiddelde van drie getallen weergeeft.

Zorg dat het gemiddelde afgerond wordt op 2 cijfers na de komma.

#### Voorbeeld
Voor de achtereenvolgende invoer `12`, `5`, `8` verschijnt:
```
maximum: 12
minimum: 5
gemiddelde: 8.33
```