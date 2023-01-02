De <a href='https://nl.wikipedia.org/wiki/Discriminant' target='_blanc'>discriminant</a> is de uitdrukking die zal bepalen of een vierkantsvergelijking al dan niet oplossingen heeft.

## Opgave

Schrijf een functie `discriminant( a, b, c )` die voor een vierkantsvergelijking $$ax^2+bx+c=0$$ de waarde van de discriminant berekent. Deze waarde wordt op het scherm op een specifieke manier **afgedrukt**. Daarna zal het programma op het scherm afdrukken of er geen, één of twee verschillende oplossingen zijn.

#### Voorbeelden
De vierkantsvergelijking $$2x^2+6x+5 = 0$$ heeft als discriminant -4.
```
>>> discriminant( 2, 6, 5 )
Discriminant = -4
Er zijn geen oplossingen
```

De vierkantsvergelijking $$x^2+x+1 = 0$$ heeft als discriminant 0.
```
>>> discriminant( 1, 2, 1 )
Discriminant = 0
Er is exact één oplossing
```

De vierkantsvergelijking $$x^2+3x-4 = 0$$ heeft als discriminant 25.
```
>>> discriminant( 1, 3, -4 )
Discriminant = 25
Er zijn twee verschillende oplossingen
```



