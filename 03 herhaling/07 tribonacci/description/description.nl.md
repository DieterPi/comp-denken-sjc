Je kan een variant maken op de rij van Fibonacci, namelijk de rij van Tribonacci, door het volgende voorschrift te gebruiken:

$$
    \mathsf{u_n = u_{n-1} + u_{n-2} + u_{n-3}, \quad\text{\textsf{waarbij}} \qquad u_0 = 0, u_1 = 0, \text{ \textsf{en} } u_2 = 1}
$$

De rij begint dan als volgt:

$$
    \mathsf{0,\quad 0,\quad 1,\quad 1,\quad 2,\quad 4,\quad 7,\quad 13,\quad 24,\quad ...}
$$

## Gevraagd
Schrijf een programma dat een rangnummer `n` aan de gebruiker vraagt. Daarna berekent je programma het n<sup>de</sup> getal in de rij van Tribonacci en toont het dit op het scherm.

#### Voorbeelden

Bij invoer `4` verschijnt:
```
Het getal uit de rij van Tribonacci met rangnummer 4 is 2
```

Bij invoer `8` verschijnt:
```
Het getal uit de rij van Tribonacci met rangnummer 8 is 24
```