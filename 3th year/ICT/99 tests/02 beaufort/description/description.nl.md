Windkracht wordt uitgedrukt in de schaal van Beaufort. Oorspronkelijk telde de schaal 13 waarden, maar sinds 1946  werd een nieuwe schaal ontwikkeld die 17 waardes telt. Men berekent de Beaufort windsnelheid $$B$$ via de volgende formule:

$$
    B = \left(\dfrac{v}{0.836}\right)^\frac{3}{2}
$$

Hierbij wordt de Beaufort windsnelheid steeds afgerond op **eenheden** nauwkeurig. 

![beaufort](media/beaufort.jpg "Een windsok"){:data-caption="Een windsok" width="40%"}

## Opgave
Schrijf een programma dat de windsnelheid in $$\dfrac{\text{m}}{\text{s}}$$ vraagt en vervolgens de Beaufort windsnelheid uitrekent.

#### Voorbeeld
Een windsterkte van $$1.2 \dfrac{\text{m}}{\text{s}}$$ leidt tot:
```
1 Beaufort
```

Een windsterkte van $$30 \dfrac{\text{m}}{\text{s}}$$ leidt tot:
```
11 Beaufort
```

{: .callout.callout-info}
> #### Tip
> Gebruik de functie `pow()` voor de macht en `int()` om het `11.0` als `11` te schrijven.