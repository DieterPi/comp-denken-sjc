Gewicht is een maat voor de **kracht** die een planeet op je lichaam uitoefent. Op aarde is de sterkte van het zwaarteveld 9,81 N/kg. De sterkte van het zwaarteveld op de maan is echter maar circa één zesde van deze op aarde, namelijk 1,622 N/kg.

![Buzz Aldrin op de maan.](media/history-in-hd.jpg "Foto door History in HD op Unsplash."){:data-caption="Buzz Aldrin op de maan." width="30%"}

Je kan schakelen tussen beide gewichten met de volgende formule

$$\text{gewicht}_\text{maan} = \dfrac{\text{gewicht}_\text{aarde}}{9,81} \cdot 1,622$$

## Opgave
Hieronder staat een stuk van een programma dat het gewicht van een persoon op aarde vraagt en vervolgens deze op de maan berekent en afdrukt.

```python
# Vraagt de gebruiker naar invoer.
gewicht_aarde = float( input( 'Geef je gewicht op aarde in:' ) )

# Voert de berekeningen uit.
gewicht_maan = round( gewicht_aarde / 9.81 * 1.622, 2 )

# Verzorgt de afdruk op het scherm.
print( 'Je gewicht op de maan is', gewicht_maan, 'N.' )
```

Pas het programma nu aan zodat ook het gewicht op Venus en Mars berekend en afgedrukt wordt. Gebruik hierbij onderstaande tabel:

| Planeet | Zwaarteveldsterkte (N/kg) |
|:--------:|-------------|
| Aarde  | 9,81 |
| Maan | 1,622 |
| Venus | 8,87 |
| Mars | 3,711 |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

#### Voorbeelden
De invoer `53.7` levert als uitvoer
```
Je gewicht op de maan is 8.88 N.
Je gewicht op Venus is 48.55 N.
Je gewicht op Mars is 20.31 N.
```

De invoer `84.1` levert als uitvoer
```
Je gewicht op de maan is 13.91 N.
Je gewicht op Venus is 76.04 N.
Je gewicht op Mars is 31.81 N.
```