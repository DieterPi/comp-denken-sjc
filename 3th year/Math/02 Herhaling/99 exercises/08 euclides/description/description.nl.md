Het algoritme van **Euclides** is één van de oudste algoritmes ter wereld. Het algoritme dat beschreven werd in <a href='https://nl.wikipedia.org/wiki/Euclides_van_Alexandri%C3%AB' target='_blanc'>zijn</a> legendarische handboek <a href='https://nl.wikipedia.org/wiki/Elementen_(Euclides)' target='_blanc'>De Elementen</a> is een efficiënte manier om de grootste gemene deler (ggd) van twee getallen te bepalen.

Het algoritme werkt als volgt:

- Noem het grootste van de twee getallen $$A$$ en het andere $$B$$
- Bepaal de rest $$R$$ bij deling van $$A$$ door $$B$$
- is $$R$$ nul, dan is $$B$$ de ggd
- indien $$R$$ niet nul is, herhaal het algoritme dan voor $$B$$ en de rest $$R$$

Een voorbeeld zal dit duidelijker maken:

Beschouw $$A = 28$$ en $$B = 16$$. Een getraind oog ziet meteen in dat de $$\text{ggd}(28,16) = 4$$. Het algoritme toepassen werkt nu als volgt:

- De rest bij deling van $$28$$ en $$16$$ is $$12$$
- De rest bij deling van $$16$$ en $$12$$ is $$4$$
- De rest bij deling van $$12$$ en $$4$$ is $$0$$, zodat $$4$$ de ggd is.

## Opgave

Schrijf een functie `ggd()` met twee gehele getallen als parameter dat de grootste gemene deler retourneert.

#### Voorbeelden
```
>> ggd( 28, 16 )
4
>> ggd( 16, 28 )
4
>> ggd( 1140, 900 )
60
```