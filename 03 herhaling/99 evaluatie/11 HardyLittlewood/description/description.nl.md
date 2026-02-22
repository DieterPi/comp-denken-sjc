<a href="https://nl.wikipedia.org/wiki/Godfrey_Harold_Hardy" target="_blank">Godfrey Hardy</a> en <a href="https://nl.wikipedia.org/wiki/John_Littlewood" target="_blank">John Littlewood</a> waren twee Britse bevriende wiskundigen die jarenlang hebben samengewerkt, vooral rond de beruchte Riemann hypothese.

![Hardy en Littlewood in New Court, Trinity College.](media/hardy-littlewood.jpg "Hardy en Littlewood in New Court, Trinity College."){:data-caption="Hardy en Littlewood in New Court, Trinity College." width="20%"}

Ze bewezen onder andere het bestaan van de tweelingconstante:

$$
    \mathsf{\prod_{p \text{\textsf{ priem}} > 2} \left(1 - \dfrac{1}{(p-1)^2}\right) \approx 0,660161\ldots}
$$

Het linkse deel stelt een product voor met p priem (maar groter dan 2), bijvoorbeeld met **vier** factoren:

$$
    \mathsf{\left(1-\dfrac{1}{({\color{#F68512}3}-1)^2}\right)\cdot \left(1-\dfrac{1}{({\color{#F68512}5}-1)^2}\right)\cdot \left(1-\dfrac{1}{({\color{#F68512}7}-1)^2}\right)\cdot \left(1-\dfrac{1}{({\color{#F68512}11}-1)^2}\right)}
$$

## Opgave

Vraag aan de gebruiker naar een bovengrens (groter dan 3). Bepaal vervolgens een benadering van deze constante door dit uit te rekenen voor de priemgetallen **kleiner** dan het opgegeven getal.

Rond het resultaat af op 9 decimalen. Geef ook het aantal factoren weer.

#### Voorbeelden

Indien de gebruiker `12` intikt, verschijnt er:
```
De benadering voor de tweelingsconstante met 4 factoren bedraagt 0.676757812
```

Indien de gebruiker `7` intikt, verschijnt er:
```
De benadering voor de tweelingsconstante met 2 factoren bedraagt 0.703125
```