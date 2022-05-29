![Speeding](media/speeding.jpg "Speeding"){:data-caption="Snelheidscontrole." width="450px"}

De politie voert een snelheidscontrole uit in de bebouwde kom. De maximum toegestane snelheid is er 50 km/u. Het aantal km dat je over die begrenzing gaat, bepaalt de boete. 

| aantal km/u overtreding | te betalen bedrag |
|:--------:|-------------|
| tot 10 km/u  | € 53 |
| 11 tot 30 km/u | € 53 en € 11 per extra overschreden km |
| meer dan 30 km/u | Tussen € 80 en € 4000, rechtszaak en invordering van het rijbewijs |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

{: .callout.callout-warning}
> #### Opgelet
> Merk op dat in de tweede categorie de eerste 10 km/u overschrijding **niet** meegerekend worden als extra overschreden km's.

## Opgave
Schrijf een functie `boete()` met de gemeten snelheid als parameter en die de totale boete **afdrukt**. Indien er **geen** overtreding werd vastgesteld verschijnt er `Niet in overtreding'.

#### Voorbeeld
```
>>> boete( 58 )
Boete: EUR 53
>>> boete( 65 )
Boete: EUR 108
>>> boete( 87 )
Invordering rijbewijs en rechtszaak
```
