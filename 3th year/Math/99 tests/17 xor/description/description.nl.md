De ANSI schematische voorstelling van een XOR-poort (ook gekend als een *exclusieve of*) is als volgt:

![De ANSI voorstelling van een XOR-poort.](media/XOR-ansi.png "Afbeelding door Inductiveload op Wikimedia."){:data-caption="De ANSI voorstelling van een XOR-poort." width="180px"}

Met onderstaande waarheidstabel:

| A | B | Q |
|:--------:|:--------:|:--------:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

## Opgave
Schrijf een functie `xor( A, B )` hetgeen gegeven twee Booleanse waarden de juiste uitvoer verzorgt. 


{: .callout.callout-danger}
> #### Opgelet
> Je programma mag **geen enkele** keuze (`if`) bevatten! Maak **enkel** gebruik van de Booleaanse operatoren `and`, `or` en `not`.


#### Voorbeelden
```
>>> xor( True, False )
True
```

```
>>> xor( False, False )
False
```