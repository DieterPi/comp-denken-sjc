Kleuren kunnen digitaal voorgesteld worden in het RGB-kleursysteem. Hierbij gebruikt men 3 bytes om de hoeveelheid <span style="color:#FF0000">**R**ood</span>, <span style="color:#00FF00">**G**roen</span> en <span style="color:#0000FF">**B**lauw</span> voor te stellen. De RGB-code (0, 128, 128) stelt bijvoorbeeld de kleur <span style="color:#008080">**groenblauw**</span> voor.

Elk van de 3 getallen in het RGB-kleursysteem kan een waarde aannemen van 0 tot en met 255. Er zijn dus telkens 2<span style="vertical-align: super;">8</span> = 256 mogelijkheden per kleurcode.

![De kleurcirkel.](media/lucas-george.jpg "Foto door Lucas George op Unsplash."){:data-caption="De kleurencirkel." width="500px"}

## Opgave
schrijf een functie `RGB()` die gegeven een RGB-code als **tupel** de afzonderlijke waarden afdrukt.

#### Voorbeeld
```
>>> RGB( (0, 128, 128) )
Rood: 0
Groen: 128
Blauw: 128
```