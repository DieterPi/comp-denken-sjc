Je kan een variant maken op de rij van Fibonacci, namelijk de rij van Tribonacci, door het volgende voorschrift te gebruiken:

$$
    \mathsf{u_n = u_{n-1} + u_{n-2} + u_{n-3}, \quad\text{\textsf{waarbij}} \qquad u_1 = 0, u_2 = 0, \text{ \textsf{en} } u_2 = 1}
$$

De rij begint dan als volgt:

$$
    \mathsf{0,\quad 0,\quad 1,\quad 1,\quad 2,\quad 4,\quad 7,\quad 13,\quad 24,\quad, ...}
$$

## Gevraagd
Schrijf een programma dat een rangnummer n aan de gebruiker vraagt. Daarna berekent je programma het n<sup>de</sup> getal in de rij van Tribonacci en toont het dit op het scherm.

#### Voorbeelden

Bij invoer `3` verschijnt:
```
Het 3e getal is 1
```

Bij invoer `9` verschijnt:
```
Het 9e getal is 24
```