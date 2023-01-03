## Opgave
Het volgende stukje code berekent het product `n · x` door herhaaldelijk de optelling te gebruiken: `n · x = x + x + x + ... + x`.

```python
n = int( input( 'n = ' ) )
x = int( input( 'x = ' ) )

product = 0
for i in  range( n ):
    product += x
print( product ) 
```

Hoe moet je deze code aanpassen zodat je er de machtsverheffing `x^n` mee kan programmeren: `x^n = x · x · x · ... · x`.


#### Voorbeelden
Bij de invoer `8` en `2` verschijnt er:
```
256
```

Voor invoer `3` en `5` verschijnt er:
```
125
```