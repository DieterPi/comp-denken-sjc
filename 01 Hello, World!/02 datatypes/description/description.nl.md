### Soorten getallen en tekst
Een computer heeft heel wat verschillende manieren om gegevens op te slaan. Python heeft verschillende datatypes om deze gegevens op te slaan.
Naast getallen zullen we allereerst met Booleaanse waarden en tekst.

#### Gehele getallen
Het meest eenvoudige zijn de gehele getallen, in het Engels noemt men dit **integers**. Met behulp van de *functie* `type()` kan je gemakkelijk achterhalen wat het type van een gegeven of variable is. Probeer bijvoorbeeld het volgende stukje code uit:

```python
x = 5
print( type( x ) )
```
Je merkt dat `x` van het type `int` is.

#### Kommagetallen
Kommagetallen, of **floating-point numbers**, zorgen voor een computer al meteen een probleem. Een computer kan moeilijk overweg met getallen die een *onbegrensde decimale vorm* hebben. Probeer het volgende stukje code uit, merk hierbij op dat komma's in Python met behulp van een **punt** geschreven worden.

```python
x = 3.5
print( type( x ) )
```
Je merkt dat `x` van het type `float` is.

Door de manier waarop Python floats opslaat, kunnen bepaalde getallen niet precies vastgelegd worden. Probeer bijvoorbeeld eens:
```python
print( (431 / 100) * 100 )
```
Wat merk je op?

#### Booleaanse waarden
Booleaanse waarden worden in wiskunde verder onder de loep genomen, het is een datatype dat enkel de waarde `True` of `False` kan aannemen en wordt vooral gebruikt bij het maken van keuzes.

```python
x = True
print( type( x ) )
```
Je merkt dat `x` van het type `bool` is.

#### Tekst
Een reeks tekens of tekst noemt men in het Engels een **string**. Werk je met tekst dan moet je die tekens steeds tussen aanhalingstekens `'` plaatsen.

```python
x = 'Expecto patronum!'
print( type( x ) )
```
Je merkt dat `x` van het type `str` is.

Een getal hoeft niet altijd van het type integer zijn. Zo heeft het bijvoorbeeld weinig zin om een huisnummer op te slaan als een geheel getal. Logischer is in dit geval:

```python
huisnummer = '7'
print( type( huisnummer ) )
```

### Opgave
d