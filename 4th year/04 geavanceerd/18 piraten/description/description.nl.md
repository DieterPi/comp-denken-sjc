![Piraten!](media/mateusz-dach.jpg "Foto door Mateausz Dach op Pexels"){:data-caption="Piraten!" width="450px"}

Volgens <a href="https://en.wikipedia.org/wiki/The_monkey_and_the_coconuts" target="_blank">een oude puzzel</a> zijn vijf piraten en hun aap gestrand op een eiland.  

Gedurende de dag verzamelen ze kokosnoten, die ze op een grote stapel leggen.  
Wanneer de nacht valt gaan ze slapen.  

Midden in de nacht wordt de eerste piraat wakker. Hij vertrouwt zijn makkers niet, dus hij verdeelt de stapel kokosnoten in vijf gelijke delen, neemt wat hij aanneemt dat zijn deel is, en verstopt dat.  
Hij houdt één kokosnoot over, en die geeft hij aan de aap.  
Dan valt hij weer in slaap.  

Een uur later wordt de tweede piraat wakker. Hij handelt net als de eerste piraat: hij verdeelt de stapel in vijf gelijke delen, neemt wat hij denkt dat zijn deel is, en verstopt dat. Ook hij houdt een kokosnoot over die hij aan de aap geeft.  
Dan valt hij weer in slaap.

Hetzelfde gebeurt met de andere drie piraten: één voor één worden ze wakker, verdelen de stapel, geven een kokosnoot aan de aap, verstoppen hun deel, en gaan weer slapen.  

In de ochtend worden ze allemaal wakker. Ze verdelen eerlijk wat er van de stapel kokosnoten over is. Deze keer is er echter **geen** kokosnoot meer over.

De vraag is: wat is het kleinste aantal kokosnoten dat er op de originele stapel kan hebben gelegen?  

## Opgave

Schrijf een Python functie `piraten_puzzel( aantal_piraten = 5 )` dat de puzzel oplost. 
Probeer dit eerst uit in het geval van vijf piraten, maar zorgt dat je programma ook werkt voor een ander aantal piraten.

#### Voorbeelden
```
>>> piraten_puzzel()
Bij 5 piraten zijn er 3121 kokosnoten nodig.
```

```
>>> piraten_puzzel( 6 )
Bij 6 piraten zijn er 233275 kokosnoten nodig.
```