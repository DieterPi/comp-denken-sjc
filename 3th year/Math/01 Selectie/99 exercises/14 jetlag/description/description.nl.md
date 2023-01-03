Iedereen die ooit al eens een lange vlucht naar het oosten of het westen heeft gemaakt, kent ongetwijfeld het fenomeen van de jetlag. Overdag voel je je moe en wil je gaan slapen, en 's nachts lig je wakker in bed. Na enkele dagen heb je je bioritme echter volledig aangepast aan de lokale omstandigheden. Om te berekenen hoeveel dagen $$d$$ je nodig hebt om te herstellen van een jetlag, ontwikkelde de Internationale Burgerluchtvaartorganisatie (<a href="https://www.icao.int/Pages/default.aspx" target="_blanc">ICAO</a>) de volgende formule:

$$d = \frac{\frac{u}{2} + (z-3) + v + a}{10}$$

Hierbij stelt $$u$$ het aantal vlieguren van de reis voor en $$z$$ het aantal tijdszones dat daarbij overbrugd wordt. Het uur van vertrek $$v$$ en aankomt $$a$$ wordt ingecalculeerd op basis van onderstaande tabellen.



| vertrek tussen | $v$ |
|:--------:|:-----------:|
| 8u00 en 12u00 | 0|
| 12u00 en 18u00 | 1 |
| 18u00 en 22u00| 3 |
| 22u00 en 1u00 | 4 |
| 1u00 en 8u00 | 5 |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}



| aankomst tussen | $a$ |
|:--------:|:-----------:|
| 8u00 en 12u00 | 4|
| 12u00 en 18u00 | 2 |
| 18u00 en 22u00| 0 |
| 22u00 en 1u00 | 1 |
| 1u00 en 8u00 | 3 |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}


De grenzen die gebruikt worden om en te bepalen zijn steeds exclusief het beginuur en inclusief het einduur. Vertrek- en aankomsttijden zijn steeds aangegeven in de lokale tijd.

![Slaap inhalen op de luchthaven.](media/joyce-romero.jpg "Foto door Joyce Romero op Unsplash."){:data-caption="Slaap inhalen op de luchthaven." width="60%"}

## Opgave
Schrijf een programma dat vier natuurlijke getallen vraagt, respectievelijk de waarden voor $$u$$, $$z$$, vertrektijd en aankomsttijd.  De vertrek- en aankomsttijden worden afgerond tot het dichtsbijzijnde uur.

Daarna print het programma het aantal dagen dat nodig is om te herstellen van de jetlag.

#### Voorbeeld
Stel bijvoorbeeld dat je van New York Kennedy Airport naar London Heathrow vliegt. Je vlucht vertrekt om 7:00 lokale tijd in New York en komt aan om 19:00 lokale tijd in Londen. Als we weten dat het in Londen vijf uur later is dan in New York, dan hebben we dus als invoer de waarden `u=7`, `z=4`, `7` en `19`. (Wat overeenkomt met `v=5` en `a=0`.)
Wat als uitvoer oplevert:
```
Je hebt 0.95 dagen nodig om te herstellen.
```

De invoer `9999` levert als uitvoer
```
Je moet maar één stap meer zetten.
```