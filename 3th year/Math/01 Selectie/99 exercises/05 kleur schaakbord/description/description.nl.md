Een schaakbord is opgebouwd uit 8 x 8 velden, telkens afwisselend van kleur: licht (wit) en donker (zwart).

![Schaakbord](media/schaakbord.png "Schaakbord"){:data-caption="De velden met coördinaten (1,1) en (2,6) hebben een zwarte kleur." width="35%"}

Elk veld wordt aangeduid door een combinatie van kolomnummer (k) en rijnummer (r). Bij het verwijzen naar een veld geven we steeds eerst het kolomnummer door en dan pas het rijnummer. De kolom helemaal links heeft kolomnummer 1, de kolom helemaal rechts heeft kolomnummer 8. De rij helemaal onderaan heeft rijnummer 1, de rij helemaal bovenaan heeft rijnummer 8.

In de figuur zie je de coördinaten (*tupels*) van twee velden. Het veld (1,1) helemaal onderaan links is een donker veld, het veld met coördinaat (2,6) is ook een donker veld.

## Opgave
Schrijf een functie `kleur()` die een coördinaat als parameter heeft (een *tupel*), en vervolgens afdrukt of dit een licht of donker veld is.

#### Voorbeeld
```
>>> kleur( (1, 1) )
Een donker gekleurd veld
>>> kleur( (2, 6) )
Een donker gekleurd veld
>>> kleur( (8, 7) )
Een licht gekleurd veld
```