De body-mass index (BMI) of Quetelet index is een statistiek die de massa van een **volwassen** persoon vergelijkt ten opzichte van zijn of haar lengte. De index werd genoemd naar de Gentenaar <a href='https://nl.wikipedia.org/wiki/Adolphe_Quetelet' target='_blanc'>Adolphe Quetelet</a> (1796-1874). 

De waarde van de index wordt bepaald als de massa van de persoon (in kilogram) gedeeld door het kwadraat van zijn of haar lengte (in meter):

$$
\text{BMI} = \dfrac{\text{massa}}{\text{lengte}^2}
$$

Zo is de BMI van een persoon van 90 kilogram met een lengte van 173 centimeter bijvoorbeeld gelijk aan 30,07.

De BMI kan strikt genomen **niet** gebruikt worden als betrouwbare maat voor het schatten van een gezond lichaamsgewicht van een persoon op basis van diens lengte, aangezien individuele verschillen in lichaamsbouw niet in rekening worden gebracht (verhouding van spier-, bot- en vetweefsel). In de dagelijkse medische praktijk is de BMI echter wel goed bruikbaar en voldoende betrouwbaar. Dit geldt met name bij grotere afwijkingen zoals ondergewicht en overgewicht. Bijgevolg wordt de BMI tegenwoordig ondermeer gebruikt door de Wereldgezondheidsorganisatie.

Onderstaande tabel geeft een manier om een BMI-waarde te interpreteren:

| BMI (kg/m²) | beschrijving |
|:--------:|-------------|
| < 18  |    ondergewicht |
| [18,25[ |  normaal gewicht |
| [25,30[ | overgewicht |
| ≥ 30 |  obesitas |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

## Opgave
Schrijf een functie `bmi()` die de massa (in kg) en de lengte (in cm) als parameters heeft, vervolgens het bmi berekent en een beschrijving afdrukt.

{: .callout.callout-info}
> #### Tip
> Om problemen met kommagetallen te vermijden laat je de berekening van het bmi best **afronden** op 2 cijfers na de komma.

#### Voorbeelden
```
>>> bmi( 90, 173 )
Een persoon van 90 kg met een lengte van 173 cm heeft obesitas.
```
```
>>> bmi( 74, 184 )
Een persoon van 74 kg met een lengte van 184 cm heeft een normaal gewicht.
```

{: .callout.callout-danger}
> #### Opgelet
> De BMI-waarde is pas zinvol indien deze toegepast wordt op **volwassenen**. Het heeft dus **geen zin** om je eigen massa en lengte te gebruiken om te testen.