## Modules
Python bezit over een groot aantal modules waar heel **wat handige functies** in voorgeprogrammeerd zitten. 

Om een module te kunnen gebruiken zet men bovenaan de code
```python
import <modulenaam>
```
### Math
De `math` module zal ons het leven veel eenvoudiger maker.

Beschouw de volgende functies die dan meteen te gebruiken vallen.
```python
import math

print( math.sqrt(36) )
print( math.pi )
print( math.ceil(4.3) )
print( math.floor(4.3) )
```

### Random
De `random` module laat ons toe willekeur toe te voegen aan programma's, de functies `randint()` en `uniform()` zullen we het vaakst gebruiken.

```python
import random

print( random.randint(0,10) )
print( random.randint(0,10) )

print( random.uniform(0,10) )
print( random.uniform(0,10) )
```
## Opgave
Het *geometrisch* of *meetkundig* gemiddelde x<span style="vertical-align:sub;">g</span> van 2 getallen a en b is gedefinieerd als:

$$
    x_g = \sqrt{a\cdot b}
$$

Schrijf een functie `meetkundig_gemiddelde( a, b )` die het meetkundig gemiddelde berekent en deze waarde afdrukt. Rond af op 2 cijfers.

#### Voorbeelden
```
>>> meetkundig_gemiddelde( 4, 25 )
10.0
```
```
>>> meetkundig_gemiddelde( 165,114 )
137.15
```
10 is op te vatten als een *gemiddelde* van 4 en 25 omdat er een getal 2,5 bestaat zodat 4 · 2,5 = 10 en 10 · 2,5 = 25.