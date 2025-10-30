## Gegeven

495 is gekend als een constante van Kaprekar, genoemd naar de Indiase wiskundige Shri Dattathreya Ramachandra Kaprekar. De eigenschap die dit getal bezit wordt aangegeven door de volgende stappen te doorlopen:

- Neem een **willekeurig** natuurlijk getal van **drie cijfers**. (*met minimaal twee verschillende cijfers*)
- Zet de cijfers in oplopende en in aflopende volgorde, zodat twee getallen van drie cijfers worden verkregen.
- Trek het kleinste van het grootste getal af.
- Keer terug naar de tweede stap.

Dit proces doorlopen zal steeds in het getal 495 eindigen. Kies bijvoorbeeld als startgetal `534`, dan geldt:

- 543 - 345 = 198
- 981 - 189 = 792
- 972 - 279 = 693
- 963 - 369 = 594
- 954 - 459 = 495

Het proces nog eens uitvoeren met 495 leidt tot: 954 - 459 = 495.

## Gevraagd

Vraag aan de gebruiker een willekeurig getal dat bestaat uit drie cijfers. Je mag ervan uitgaan dat de gebruiker steeds een geldig getal intikt.

Geef vervolgens de Kaprekar berekening weer. Stop indien je `495` bekomt.

#### Voorbeelden

Bij invoer: `534` verschijnt:

```
Startgetal: 534
Na stap 1: 198
Na stap 2: 792
Na stap 3: 693
Na stap 4: 594
Na stap 5: 495
```