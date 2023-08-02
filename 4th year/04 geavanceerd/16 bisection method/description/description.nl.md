De bisectiemethode is een iteratieve methode voor het bepalen van nulwaarden van continue functies op een interval waarbij de functiewaarden op de grenzen van dit interval een verschillend teken hebben.

Om bijvoorbeeld een nulwaarde van de functie $$F(x)$$ te bepalen op het interval $$[a,b]$$ gaat men als volgt te werk. In dit voorbeeld geldt $$F(a) > 0$$ en $$F(b) <0$$.

- Men bepaalt het midden $$c = \dfrac{a+b}{2}$$ van dit interval en berekent er de functiewaarde. 
- Is deze positief dan ligt een nulwaarde tussen $$[c,b]$$, is deze echter negatief dan ligt een nulwaarde in het interval $$[a,c]$$.
- Herhaal deze methode op het interval $$[a,c]$$ of $$[c,b]$$ afhankelijk van bovenstaande berekening.

Vaak zal de methode niet exact eindigen, maar is men tevreden indien voor een potentiële nulwaarde $$c$$ geldt dat $$F(c)$$ voldoende dicht van nul ligt. Men gebruikt hiervoor de breedte van het interval waartussen gezocht wordt.

![Bisectiemethode](media/animation.gif "De bisectiemethode"){:data-caption="Animatie door D. Vanderfaeillie." width="1593px"}

## Opgave

Schrijf een functie `bisectiemethode( f, a, b, toleratie)` waarbij `f` een continue functie voorstelt met een nulwaarde van oneven orde, `a` en `b` respectievelijk de linker- en rechtergrenzen en `toleratie` de breedte van het interval waarop men zoekt. Hoe kleiner de toleratie, hoe nauwkeurig de methode.

De functie retourneert de nulwaarde tot op 4 cijfers na de komma nauwkeurig.

#### Voorbeelden
```
>>> def f( x ) : return x - 2
>>> bisectiemethode( f, 0, 5, 10**-4)
2.0
```

```
>>> def f( x ) : return x** 3 - 2
>>> bisectiemethode( f, 1, 4, 10**-5)
1.2599
```