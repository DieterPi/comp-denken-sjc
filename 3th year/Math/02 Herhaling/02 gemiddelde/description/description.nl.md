## Opgave
In de lessen ICT werd het harmonisch gemiddelde van twee getallen bepaald. 
Schrijf twee functies `rekenkundige_gemiddelde( tupel )` en `harmonisch_gemiddelde( tupel )` die voor een gegeven tupel met willekeurige lengte de respectievelijke gemiddeldes **retourneert**. De gemiddeldes worden steeds afgerond op 2 cijfers na de komma.

De definities van rekenkundig $$\overline x$$ en harmonisch $$x_h$$ gemiddelde voor een tupel $$(x_1,x_2,x_3, \ldots, x_n)$$ zijn als volgt:

$$
\overline x = \dfrac{1}{n}(x_1+x_2+\ldots+x_n)\qquad\qquad x_h = \dfrac{n}{\frac{1}{x_1}+\frac{1}{x_2}+\ldots+\frac{1}{x_n}}
$$

Hierbij zijn $$x_1, x_2, \ldots, x_n$$ strikt positieve reële getallen. (omwille van de definitie van het harmonisch gemiddelde)

#### Voorbeeld
Er geldt:
```
>>> rekenkundig_gemiddelde((100, 120))
110.0
>>> harmonisch_gemiddelde((100, 120))
109.09
```
Maar evengoed voor een langere rij getallen:
```
>>> rekenkundig_gemiddelde((35, 46, 39, 26, 20, 45, 30, 26, 35))
33.56
>>> harmonisch_gemiddelde((35, 46, 39, 26, 20, 45, 30, 26, 35))
31.36
```