De spons van Menger is een voorbeeld van een driedimensionale fractaal. Deze fractaal werd bedacht door Karl Menger, een Oostenrijks-Amerikaanse wiskundige.

Hieronder zie je de eerste vijf iteraties uit de constructie van deze fractaal.

![Animatie door Datumizer op Wikimedia Commons](media/Menger.gif "Animatie door Datumizer op Wikimedia Commons"){:data-caption="Animatie door Datumizer op Wikimedia Commons" width="400px"}

In iedere stap wordt elk vierkant verdeeld in 9 kleinere vierkanten die toelaten om de kubussen uit elk vlak (**en** de kubus in het midden) te verwijderen. Het resultaat is een *sponsachtige* figuur.

## Opgave

Schrijf een programma dat aan de gebruiker de lengte van de ribbe (kommagetal) van het de eerste kubus vraagt en nadien het nummer in de iteratie.

Vervolgens bereken je na elke iteratie uit hoeveel kubussen de figuur is opgebouwd en wat het totale volume is van de figuur. **Rond** hierbij telkens af op 4 decimalen.

#### Voorbeelden

Meet de startribbe `3.0` cm en wil je de berekeningen tot en met iteratie `4`, dan verschijnt er:

```
De startkubus heeft een volume van 27.0 cm³.
Na stap 1 zijn er 20 kubussen in het totaal en is het totale volume 20.0 cm³.
Na stap 2 zijn er 400 kubussen in het totaal en is het totale volume 14.8148 cm³.
Na stap 3 zijn er 8000 kubussen in het totaal en is het totale volume 10.9739 cm³.
Na stap 4 zijn er 160000 kubussen in het totaal en is het totale volume 8.1288 cm³.
```

Meet de startribbe `28.4` cm en wil je de berekeningen tot en met  iteratie `9`, dan verschijnt er:

```
De startkubus heeft een volume van 22906.304 cm³.
Na stap 1 zijn er 20 kubussen in het totaal en is het totale volume 16967.6326 cm³.
Na stap 2 zijn er 400 kubussen in het totaal en is het totale volume 12568.6167 cm³.
Na stap 3 zijn er 8000 kubussen in het totaal en is het totale volume 9310.0865 cm³.
Na stap 4 zijn er 160000 kubussen in het totaal en is het totale volume 6896.3603 cm³.
Na stap 5 zijn er 3200000 kubussen in het totaal en is het totale volume 5108.4151 cm³.
Na stap 6 zijn er 64000000 kubussen in het totaal en is het totale volume 3784.0112 cm³.
Na stap 7 zijn er 1280000000 kubussen in het totaal en is het totale volume 2802.9712 cm³.
Na stap 8 zijn er 25600000000 kubussen in het totaal en is het totale volume 2076.275 cm³.
Na stap 9 zijn er 512000000000 kubussen in het totaal en is het totale volume 1537.9815 cm³.
```
