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
Schrijf een functie `xor( A, B )` hetgeen geven twee Booleanse waarden de juiste uitvoer verzorgt. 

Zorg dat je programma **geen enkele** `if` bevat, gebruik **enkel** de Booleaanse operatoren `and`, `or` en `not`.

#### Voorbeelden
```
>>> xor( True, False )
True
```

```
>>> xor( False, False )
False
```