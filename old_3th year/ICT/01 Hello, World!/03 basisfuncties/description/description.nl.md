## Basisfuncties
Functies vormen een **essentieel** onderdeel van het programmeren. Je hebt in de vorige lessen al enkele basisfuncties gebruikt. Zo geeft de functie `print()` iets weer op het scherm. De functie `type()` bepaalt dan weer een datatype.

Later zullen we zelf eigen functies gaan samenstellen, maar eerst zal het handig zijn om kennis te maken met enkele functies die Python reeds voor ons klaar heeft.

### Handige basisfuncties
Handige functies die we meteen kunnen gebruiken zijn `abs()`, `min()` en `max()`, `pow()` en `round()`. Beoordeel zelf wat het nut van deze functies in met behulp van het vorige voorbeeld.

```python
x = -2
y = 3
z = 1.27

print( 'abs( x ):', abs( x ) )
print( 'max( x, y, z ):', max( x, y, z ) )
print( 'min( x, y, z ):', min( x, y, z ) )
print( 'pow( x, y ):', pow( x, y ) )
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