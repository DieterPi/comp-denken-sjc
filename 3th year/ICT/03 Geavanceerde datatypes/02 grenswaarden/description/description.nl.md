## Opgave
Schrijf een programma dat van een kommagetal $$x$$ het grootste geheel getal $$z$$ en kleinste geheel getal $$y$$ bepaalt zodat:

$$
y \leqslant x < z
$$

Geef de drie getallen in die volgorde daarna weer in een lijst.

{: .callout.callout-info}
> #### Tip
> Gebruik de functie `floor()` uit de module `math`.

#### Voorbeelden
Voor de invoer `4.7` verschijnt:
```
[4, 4.7, 5]
```

Voor de invoer `-5.2` verschijnt:
```
[-6, -5.2, -5]
```


Voor de invoer `1` verschijnt:
```
[1, 1.0, 2]
```