De <a href="https://nl.wikipedia.org/wiki/Rij_van_Padovan" target="_blank">rij van Padovan</a> is een rij natuurlijke getallen die gedefinieerd wordt met als eerste drie getallen telkens 1.

Daarna worden de getallen gevormd door het **voorlaatste** getal en het **derde laatste** getal op te tellen. Je kan dit grafisch voorstellen als de **zijden** van een gelijkzijdige driehoek die telkens opgebouwd werd uit de vorige gelijkzijdige driehoeken.

![De rij van Padovan](media/image.png "De rij van Padovan"){:data-caption="De rij van Padovan" width="400px" .light-only }

![De rij van Padovan](media/image_dark.png "De rij van Padovan"){:data-caption="De rij van Padovan" width="400px" .dark-only }

Men krijgt dus als rij:

$$
\mathsf{1, \quad 1, \quad 1, \quad 2, \quad 2, \quad 3, \quad 4, \quad 5, \quad 7, \quad 9, \quad 12, \quad \ldots}
$$

Het element 7 wordt bijvoorbeeld gevormd door het getal 3 en 4 op te tellen. 9 wordt gevormd door de getallen 4 en 5 op te tellen, enz...

Je kan dit wiskundig noteren via onderstaand voorschrift:

$$
 \mathsf{u_n = u_{n-2}+u_{n-3}, \qquad\text{\textsf{met}}\qquad u_1 = 1, u_2=1 \text{ \textsf{en} } u_3 = 1}
$$

## Opgave
Schrijf een programma dat een rangnummer `n` aan de gebruiker vraagt. Daarna berekent je programma het n<sup>de</sup> getal in de rij van Fibonnaci en toont het dit op het scherm.

#### Voorbeelden

Bij invoer `3` verschijnt:
```
Het 3e getal is 1
```

Bij invoer `6` verschijnt:
```
Het 6e getal is 3
```

Bij invoer `9` verschijnt:
```
Het 9e getal is 7
```

{: .callout.callout-info}
> #### Tip
> Maak gebruik van de selectie om de eerste drie rangnummers apart op te vangen.