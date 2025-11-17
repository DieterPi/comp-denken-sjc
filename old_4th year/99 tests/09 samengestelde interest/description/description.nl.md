> Samengestelde interest is het 8e wereldwonder. Hij die het begrijpt, verdient het... hij die het niet begrijpt, betaalt het...
>
> *Albert Einstein*

Bij een belegging met samengestelde interest wordt de jaarlijkse rente **terug** in je belegging geïnvesteerd. Op die manier word je het jaar nadien beloond met een rente op de rente die je het jaar voordien kreeg. 

Stel bijvoorbeeld dat je € 10 000 belegd met een rendement van 3% per jaar:

- Na het eerste jaar wordt de winst, € 300 opnieuw aan de belegging toegevoegd, er zit dan dus € 10 300 in de belegging.
- Na het tweede jaar wordt aan dit bedrag opnieuw 3% rendement toegevoegd, nu is dit € 309, zodat er € 10 609 belegd staat.
- Het jaar nadien is de winst € 318,27 zodat er € 10 927,27 in de belegging aanwezig is.

Ga je zo verder dan zal er na 15 jaar ca. € 15 579,67 aanwezig zijn.

Had je elk jaar *slechts* 3% rendement op het *oorspronkelijke bedrag* gekregen dan was het totaalbedrag na 15 jaar slechts € 14 500.

## Opgave
Schrijf een functie `samengesteld( startbedrag, rentevoet, aantal_jaar )` die stap per stap het eindbedrag berekent bij een samengestelde belegging.

Beëindigd de functie met een zin die aangeeft hoeveel winst er werd behaald en met hoeveel procent dit jaarlijks overeenkomt. Rond in je berekeningen steeds af op 2 cijfers na de komma.

#### Voorbeeld
```
>>> samengesteld( 10000, 0.03, 15 )
Na jaar 1 is het bedrag aangegroeid tot € 10300.0
Na jaar 2 is het bedrag aangegroeid tot € 10609.0
Na jaar 3 is het bedrag aangegroeid tot € 10927.27
Na jaar 4 is het bedrag aangegroeid tot € 11255.09
Na jaar 5 is het bedrag aangegroeid tot € 11592.74
Na jaar 6 is het bedrag aangegroeid tot € 11940.52
Na jaar 7 is het bedrag aangegroeid tot € 12298.74
Na jaar 8 is het bedrag aangegroeid tot € 12667.7
Na jaar 9 is het bedrag aangegroeid tot € 13047.73
Na jaar 10 is het bedrag aangegroeid tot € 13439.16
Na jaar 11 is het bedrag aangegroeid tot € 13842.33
Na jaar 12 is het bedrag aangegroeid tot € 14257.6
Na jaar 13 is het bedrag aangegroeid tot € 14685.33
Na jaar 14 is het bedrag aangegroeid tot € 15125.89
Na jaar 15 is het bedrag aangegroeid tot € 15579.67
Dit komt overeen met een winst van € 5579.67 of op jaarbasis 3.72 %.
```