## De voorwaardelijke herhaling
Soms wil je instructies herhalen, maar weet je op voorhand niet hoe vaak. In dit geval kan een voorwaardelijke herhaling een oplossing vormen.

In Minecraft konden we de agent vooruit laten bewegen **zolang** er die geen blok detecteerde voor zich, dit deden we als volgt.

![minecraft voorwaardelijke herhaling](media/voorwaardelijke_herhaling_minecraft.png "minecraft voorwaardelijke herhaling"){:data-caption="Een voorwaardelijke herhaling in Minecraft Education Edition" width="354px"}

Deze soort herhaling kan ook uitgevoerd worden in Python. Beschouw eerst het volgende voorbeeld uit Minecraft:

![minecraft voorwaardelijke herhaling](media/voorwaardelijke_herhaling.png "minecraft voorwaardelijke herhaling"){:data-caption="Een voorwaardelijke herhaling in Minecraft Education Edition" width="298px"}

In Python wordt dit gecodeerd met een `while`-loop:
```python
getal = 0
while getal <= 5:
    print( getal )
    getal += 1
```

Dit zouden we natuurlijk ook kunnen programmeren met behulp van een `for`-loop:
```python
for getal in range( 6 ):
    print( getal )
```

Toch zal je niet elke `while`-loop kunnen schrijven met behulp van een `for`-loop, omgekeerd kan dit wel.



## Opgave
