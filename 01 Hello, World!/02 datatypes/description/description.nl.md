### Soorten getallen en tekst
Een computer heeft heel wat verschillende manieren om gegevens op te slaan. Python heeft verschillende datatypes om deze gegevens op te slaan.
Naast getallen zullen we allereerst ook werken met tekst en met Booleaanse waarden.

#### Gehele getallen
Het meest eenvoudige zijn de gehele getallen, in het Engels noemt men dit **integers**. Met behulp van de *functie* `type()` kan je gemakkelijk achterhalen wat het type van een gegeven of variable is. Probeer bijvoorbeeld het volgende stukje code uit:

```python
x = 5
print( type( x ))
```

#### Kommagetallen
Kommagetallen, of **floating-point numbers**, zorgen voor een computer al meteen een probleem. Een computer kan moeilijk overweg met getallen die een *onbegrensde decimale vorm* hebben. Probeer het volgende stukje code uit, merk hierbij op dat komma's in Python met behulp van een **punt** geschreven worden.

```python
x = 3.5
print( type( x ))
```

Door de manier waarop Python floats opslaat, kunnen bepaalde getallen
niet precies vastgelegd worden. Bijvoorbeeld, het statement
`print( (431 / 100) * 100 )` geeft als antwoord 430.99999999999994, en
niet 431 zoals je zou verwachten. Als je weet dat de uitkomst van een
berekening waarin floats zitten een integer moet zijn, dan doe je er
goed aan om de uitkomst af te ronden naar het dichtstbijzijnde gehele
getal. 