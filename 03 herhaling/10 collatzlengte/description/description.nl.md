Bij het vermoeden van Collatz werd deze werkwijze gehanteerd, gegeven een natuurlijk getal (verschillend van 0):

- is het getal even, halveer het dan;
- is het getal oneven, neem dan het drievoud en tel er één bij op;

Indien het startgetal 6 is, dan resulteert dit in de volgende rij: 6 ➔ 3 ➔ 10 ➔ 5 ➔ 16 ➔ 8 ➔ 4 ➔ 2 ➔ 1

Men zegt dat de **Collatzlengte** van deze rij 9 bedraagt. Er staan immers 9 getallen in deze rij.

## Opgave

Schrijf een programma dat aan de gebruiker het startgetal vraagt en nadien de **Collatzlengte** bepaalt.

#### Voorbeelden

Bij invoer `6` verschijnt er:
```
De Collatzlengte van 6 is 9
```

Bij invoer `27` verschijnt er:
```
De Collatzlengte van 27 is 112
```