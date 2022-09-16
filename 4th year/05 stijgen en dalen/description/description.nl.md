Vorig jaar heb je de selectiestructuur leren programmeren in Python. Een voorbeeld van een programma met een selectiestructuur is het volgende. Begrijp je nog wat er hier gebeurt?

```python
leeftijd = float( input( 'Geef je leeftijd in: ' ) )

if leeftijd < 12:
    print( 'Je mag gratis op de trein!' )
elif leeftijd >= 65:
    print( 'Je krijgt 50% korting.' )
else: 
    print( 'Je moet een ticket kopen.' )
```

De basissyntax van een selectiestructuur is dus:
```python
if <voorwaarde_1>:
    <acties>
elif <voorwaarde_2>:
    <acties>
else: 
    <acties>
```

## Opgave
Bij deze oefening vul je onderstaande functie aan zodat de functie `soort_rechte( rico )` voor een gegeven rico op het scherm **afdrukt** of deze rechte stijgend, dalend of constant is. Er verschijnt respectievelijk `De rechte is stijgend.`, `De rechte is dalend.` en `De rechte is constant.`.
 
![Evenwijdige rechten](media/lines.jpg "Evenwijdige rechten"){:data-caption="Evenwijdige dalende rechten." width="400px"}

#### Voorbeelden
Bij een rico van 4 verschijnt er:
```
>>> soort_rechte( 4 )
De rechte is stijgend.
```
