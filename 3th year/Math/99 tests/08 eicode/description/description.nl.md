In de meeste Europeese landen zijn alle eieren die verkocht worden voorzien van een eicode. Met behulp van een stempel kan men zo terugvinden waar ze vandaan komen en hoe ze geproduceerd werden.

![Een krat eieren.](media/jakub-kapusnak.jpg "Foto door Jakub Kapusnak op Unsplash."){:data-caption="Een krat eieren." width="450px"}

Zo'n eicode ziet er bijvoorbeeld uit als volgt:
<div class="dodona-centered-group">
1-UK-5432102
</div>
Het eerste getal geeft aan hoe het ei geproduceerd werd. Hier is dit 1, het ei komt dus van een kip die *vrije uitloop* had. De volgende 2 karakters vormen een landcode, in dit geval het Verenigd Koninkrijk. Het *cijfer* dat hierna volgt, hier is dit 5432114, is een identificatie van de boerderij. De eerste vijf cijfers zijn een bedrijfscode (54321), de laatste twee vormen het stalnummer (02).

De mogelijke productiemethodes zijn. (Code 3 zal je binnen de supermarkt niet aantreffen.)

| getal | betekenis |
|:--------:|--------|
| 0 | biologisch ei |
| 1 | vrije-uitloopei |
| 2 | scharrelei |
| 3 | koloniehuisvesting |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

## Opgave
Schrijf een functie `eicode()` wat gegeven een *eicode* een beschrijving van de herkomst afdrukt.

#### Voorbeelden
```
>>> eicode( 1-UK-5432102 )
Vrij-uitloopei
Afkomst: Verenigd Koninkrijk
Bedrijf- en stalcode: 54321 - 02
```

```
>>> eicode( 3-NL-0451201 )
Koloniehuisvesting
Afkomst: Nederland
Bedrijf- en stalcode: 04512 - 01
```

{: .callout.callout-info}
> #### Tip
> Om de eerste karakters een stuk tekst te bepalen gebruik je vierkante haakjes. Beschouw bijvoorbeeld het volgende stukje code:
> ```python
tekst = 'College'
print( tekst[1:5] ) 
```
> Dit print de tekst `olle` af. Gebruik dus `[begin:einde]` om bepaalde stukken te selecteren.