## Opgave
De zeef van **Eratosthenes** is a methode om alle priemgetallen te vinden tussen 1 en een gegeven getal. Eratosthenes was een Griekse geleerde werkzaam aan de bibliotheek van Alexandrië.

De methode werkt als volgt. Je begint met een **lijst** te maken die bestaat uit de getallen 1 tot en met een zeker "hoogste getal." Zet de waarde van 1 op nul, omdat 1 geen priemgetal is. Verwerk nu de list in een lus. Zoek naar het eerste nummer dat niet op 0 staat, wat nummer 2 is. Dat betekent dat 2 een priemgetal is, maar alle
veelvouden van 2 zijn dat niet. Dus zet alle veelvouden van 2 op 0. Zoek dan naar het volgende nummer dat geen nul is, en dat is 3. Zet alle veelvouden van 3 op nul. Zoek dan naar het volgende nummer dat geen nul is, en dat is 5. Zet alle veelvouden van 5 op nul. Verwerk zo de hele list. Als je klaar bent, zijn alleen nog de getallen over die priemgetallen zijn. Gebruik deze methode om alle priemgetallen tussen 1 en 100 te bepalen.

Hieronder zie je de methode uitgevoerd op een lijst met getallen tot 120.
![Sieve of Eratosthenes](media/sieve.gif "Sieve of Eratosthenes"){:data-caption="De zeef van Eratosthenes" width="445px"}

#### Voorbeelden
Voor de invoer `50` verschijnt:
```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```
Voor de invoer `100` verschijnt:
```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```