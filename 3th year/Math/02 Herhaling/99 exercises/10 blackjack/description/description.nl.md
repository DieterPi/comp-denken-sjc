Het casino-spelletje Black Jack (of 21-en) is heel eenvoudig. Je krijgt twee kaarten met waarden van 1 tot en met 11. Vervolgens mag je onbeperkt kaarten bijvragen of stoppen. De speler die het dichtst bij 21 eindigt, is de winnaar. Heb je meer dan 21 dan ben je verbrand en sowieso verloren.

![Blackjack](media/blackjack.jpg "Blackjack"){:data-caption="Een aas is 11 punten en een boer 10 punten. Dit is dus een score van 21, de speler is gewonnen!" width="35%"}

## Opgave
Schrijf een programma dat de speler 2 willekeurige getallen tussen 1 en 11 geeft.

Nadien krijgt de speler de keuze, 'Verdergaan?'. Waarop de speler kan antwoorden: 'J' (Ja) of 'N' (Nee)

- Bij 'N' eindigt het spel en wordt de som van de kaarten op het scherm weergegeven.
- Bij 'J' krijgt de speler opnieuw een willekeurig getal tussen 1 en 11
    - Is de som van alle kaarten groter dan 21, dan stop het en verschijnt de som en de boodschap 'Verloren'
    - Is de som gelijk aan 21, dan verschijnt de som en de boodschap 'Gewonnen!'
    - Is de som kleiner dan 21, dan wordt opnieuw gevraagd 'Verdergaan?', enz...

#### Voorbeeld



{: .callout.callout-info}
> #### Tip
> Gebruik `import random` en `random.randint( 1, 11 )` om een willekeurig getal tussen 1 en 11 te genereren.