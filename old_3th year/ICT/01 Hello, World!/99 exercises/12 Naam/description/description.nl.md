De functie `print()` accepteert meerdere **argumenten** of **parameters**, probeer bijvoorbeeld de volgende code uit:

```python
pi = 3.14159
print( 'Het getal pi is afgerond op 5 cijfers:', pi )
```

De functie `type()` aanvaardt daarentegen slechts één argument. Namelijk het argument waarvan je het datatype wil bepalen. Probeer bijvoorbeeld eens de volgende code uit:
```python
x = 5
y = 1.5
print( type( x, y ) )
```

Een zeer handige functie is `input()`. Met behulp van die functie kan je de gebruiker om een **invoer** vragen. Test het meteen eens uit via:
```python
x = float( input( 'Geef een getal in: ' ) )
print( 'Het dubbele van', x, 'is', 2 * x )
```
Controleer wat er gebeurt indien je `float()` weglaat.

## Opgave
Schrijf een programma dat je voornaam en klas vraagt. En vervolgens een begroeting afdrukt van de vorm `Welkom voornaam uit klas !`.

#### Voorbeeld
Stel dat de gebruiker de naam `Jan` ingeeft en als klas `3LA1` dan verschijnt er:
```
Welkom Jan uit 3LA1 !
```

{: .callout.callout-info}
> #### Tip
> De `print()` functie accepteert meerdere argumenten of parameters, je kan dus gebruik maken van `print( 'Welkom', voornaam, 'uit', ...)` (vul zelf verder aan).