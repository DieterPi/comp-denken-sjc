## Opgave
Beschouw onderstaande **lijst** opgebouwd uit tupels van leerlingen en hun favoriete kleur.

Schrijf een functie `favoriete_kleur()` met een kleur als parameter die afdrukt hoeveel leerlingen die kleur als favoriete kleur hebben.

#### Voorbeelden
```
>>> favoriete_kleur( 'rood' )
8
```

```
>>> favoriete_kleur( 'oranje' )
12
```

{: .callout.callout-info}
> #### Tip
> Je kan opnieuw eenvoudig over de lijst itereren. Beschouw het onderstaande voorbeeld waarbij van een lijst met tupels telkens **het tweede element** uit de tupels afgedrukt worden.
> ```python
lijst = [ ('a', 1), ('b', -2), ('c', 0) ]
for tupel in lijst:
    print( tupel[1] )
```