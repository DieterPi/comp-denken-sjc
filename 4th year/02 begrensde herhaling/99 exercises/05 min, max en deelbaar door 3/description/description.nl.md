## Opgave
Schrijf een programma dat de gebruiker vraagt om 5 gehele getallen en vervolgens de grootste, de kleinste, en het aantal deelbaar door 3 afdrukt.

#### Voorbeeld
Na achtereenvolgende invoer van `3`, `-2`, `6`, `0` en `-7` verschijnt er:
```
Grootste getal: 6
Kleinste getal: -7
Aantal getallen deelbaar door 3: 2
```

{: .callout.callout-info}
> #### Tip
> In de module `math` zit een constante `math.inf` die je kan gebruiken bij de initialisatie. Als je de variabele `minimum` hier eerst aan gelijk stelt kan je in je programma vergelijken met deze waarde. Indien de invoer kleiner is dan de variabele, dan wordt dat het nieuwe minimum. Werk analoog voor het maximum.