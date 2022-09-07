Een vierkantsvergelijking is een vergelijking van de vorm:

$$ax^2+bx+c = 0 \qquad \text{met } a\not = 0$$

Indien echter $$b$$ of $$c$$ nul zijn noemt men dit een **onvolledige** vierkantsvergelijking. In alle andere gevallen noemt men de vierkantsvergelijking **volledig**.

## Opgave

Schrijf een functie `soort_vkv( b, c )` die voor een vierkantsvergelijking $$ax^2+bx+c=0$$ nagaat of deze vierkantsvergelijking al dan niet volledig is. De functie drukt dit op het scherm af.

#### Voorbeelden
De vierkantsvergelijking $$x^2-4 = 0$$ is onvolledig.
```
>>> >>> soort_vkv( 0, -4 )
Onvolledig
```

De vierkantsvergelijking $$x^2+2x+1 = 0$$ is volledig.
```
>>> soort_vkv( 2, 1 )
Volledig
```