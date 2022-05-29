![Triangle](media/triangle_builder.jpg "Triangle"){:data-caption="Ook in de bouw is de stelling van Pythagoras belangrijk." width="450px"}

Naast een classificatie op basis van zijden kan je een driehoek ook onderverdelen op basis van de hoeken. De driehoek kan namelijk scherphoekig, rechthoekig of stomphoekig zijn.

{: .callout.callout-secondary}
> #### Classificatie op basis van hoeken
> Indien in een driehoek met langste zijde $$x$$ en andere zijden $$y$$ en $$z$$ geldt dat $$x^2 < y^2+z^2$$ dan is de driehoek scherphoekig. Indien $$x^2=y^2+z^2$$ of $$x^2 > y^2+z^2$$, dan is de driehoek respectievelijk rechthoekig of stomphoekig.

## Opgave
Schrijf een functie `soort_driehoek()` met **drie** lengtes als parameter waarbij het programma afdrukt of de driehoek scherphoekig, rechthoekig of stomphoekig is.

#### Voorbeeld
```
>>> soort_driehoek( 3, 4 ,5 )
De driehoek is rechthoekig.
>>> soort_driehoek( 5, 4, 5 )
De driehoek is niet rechthoekig.
```
