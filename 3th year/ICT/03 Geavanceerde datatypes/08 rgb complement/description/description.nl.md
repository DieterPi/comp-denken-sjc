In kleurtheorie zijn complementaire kleuren, kleuren die sterk contrasteren. Deze kleuren staan tegenover elkaar staan in de <a href="https://nl.wikipedia.org/wiki/Kleurencirkel" target="_blanc">*kleurencirkel*</a>. Zo zijn <span style="color:#0392CE">**lichtblauw**</span> en <span style="color:#FD5308">**oranje**</span> bijvoorbeeld complementaire kleuren.

![De kleurencirkel.](media/color-wheel.png "Afbeelding door Sakurambo op Wikipedia."){:data-caption="De kleurencirkel." width="300px"}

## Opgave
schrijf een functie `complementair()` die gegeven een RGB-kleurcode als tupel de complementaire code afdrukt. Je kan kan de complementaire kleur berekenen via de formule:

<div class="dodona-centered-group">
(255 - <span style="color:#FF0000">rood</span>, 255 - <span style="color:#00FF00">groen</span>, 255 - <span style="color:#0000FF">blauw</span>)
</div>

Het is natuurlijk wel zo dat elke kleurcode uiteindelijk opnieuw een waarde van 0 tot en met 255 moet aannemen.
#### Voorbeeld
```
>>> complementair( (0, 128, 128) )
(255, 127, 127)
```

{: .callout.callout-info}
> #### Tip
> Gebruik de modulo operator `%`.