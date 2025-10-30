## Gegeven

In deze opgave wordt van een natuurlijk getal de **NIO-limiet** bepaald. Dat gaat als volgt:

- Van een natuurlijk getal wordt **eerst** het **NIO-nummer** berekend. Dat NIO-nummer krijg je door de cijfers uit het getal op een gewogen wijze bij elkaar op te tellen.

  Namelijk: 1 maal het eerste cijfer, 2 maal het tweede cijfer, 3 maal het derde cijfer, etc.

  Er geldt bijvoorbeeld dat het NIO-nummer van <span style="color:#FF8E27">2</span><span style="color:#2798ff">0</span><span style="color:#27ff8e">2</span><span style="color:#fa27ff">5</span> gelijk is aan 1 · <span style="color:#FF8E27">2</span> + 2 · <span style="color:#2798ff">0</span> + 3 · <span style="color:#27ff8e">2</span> + 4 · <span style="color:#fa27ff">5</span> = 28. 

- Dit NIO-nummer is opnieuw een natuurlijk getal en je kan hiervan dus opnieuw het NIO-nummer bepalen.

- Dit kun je herhalen tot je steeds hetzelfde getal krijgt. Dat getal noemt men de **NIO-limiet** van het startgetal.

Zo geldt bijvoorbeeld:

- Het NIO-nummer van 2025 is 28. 
- Het NIO-nummer van <span style="color:#FF8E27">2</span><span style="color:#2798ff">8</span> is 1 · <span style="color:#FF8E27">2</span> + 2 · <span style="color:#2798ff">8</span> = 18. 
- Het NIO-nummer van <span style="color:#FF8E27">1</span><span style="color:#2798ff">8</span> is 1 · <span style="color:#FF8E27">1</span> + 2 · <span style="color:#2798ff">8</span> = 17. 
- Het NIO-nummer van <span style="color:#FF8E27">1</span><span style="color:#2798ff">7</span> is 1 · <span style="color:#FF8E27">1</span> + 2 · <span style="color:#2798ff">7</span> = 15. 
- Het NIO-nummer van <span style="color:#FF8E27">1</span><span style="color:#2798ff">5</span> is 1 · <span style="color:#FF8E27">1</span> + 2 · <span style="color:#2798ff">5</span> = 11. 
- Het NIO-nummer van <span style="color:#FF8E27">1</span><span style="color:#2798ff">1</span> is 1 · <span style="color:#FF8E27">1</span> + 2 · <span style="color:#2798ff">1</span> = 3. 

  Als je nu telkens opnieuw het NIO-nummer gaat bepalen dan blijf dit 3. 

Er geldt dus dat 3 de NIO-limiet van 2025 is.

## Gevraagd

Schrijf een functie `nio_nummer(getal)` dat van een willekeurig natuurlijk getal het NIO-nummer retourneert. 

Schrijf daarna een functie `nio_limiet(getal)` dat de NIO-limiet van het getal bepaalt. Je gebruikt hierin natuurlijk de vorige functie `nio_nummer(getal)`.

#### Voorbeelden


```python
>>> nio_nummer(2025)
28
```

```python
>>> nio_nummer(28)
18
```

```python
>>> nio_nummer(18)
17
```

en

```python
>>> nio_limiet(2025)
3
```

{: .callout.callout-secondary}
>#### Bron
> Nederlandse Informatica Olympiade 2024-2025