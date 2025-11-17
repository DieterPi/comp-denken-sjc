Trilateratie wordt gebruikt om de locatie van je mobiele telefoon vast te leggen. Een gsm verstuurt constant radio signalen die opgepikt worden door drie of meer zendmasten. Met behulp van de coördinaten van deze zendmasten en de geschatte afstand van de gsm tot de zendmast (met behulp van de vertraging tussen zenden en ontvangen van een signaal) kan men de coördinaat van het snijpunt gaan berekenen. (in de praktijk schatten)

Om de situatie te vereenvoudigen wordt hieronder het tweedimensionale geval besproken.

![Trilateratie](media/image.png "Trilateratie"){:data-caption="Trilateratie van een mobiele telefoon." width="50%"}

Op het bovenstaande schema zie je hoe de drie cirkels een gemeenschappelijk snijpunt hebben. Het is de coördinaat van dat snijpunt $$(x_{\text{M}},y_{\text{M}})$$ wat gezocht moet worden.

#### Stap 1

De drie cirkels hebben telkens een vergelijking van de vorm:

$$
\begin{array}{rcl}
(x-x_1)^2 + (y-y_1)^2 & = & r_1^2\\
(x-x_2)^2 + (y-y_2)^2 & = & r_2^2\\
(x-x_3)^2 + (y-y_3)^2 & = & r_3^2
\end{array}
$$

#### Stap 2

Men kan deze drie vergelijkingen telkens uitwerken, gebruik makende van de merkwaardige producten bekomt men:

$$
\begin{array}{rcl}
x^2 - 2x_1 x + x_1^2 + y^2 - 2y_1 y + y_1^2 & = & r_1^2\\
x^2 - 2x_2 x + x_2^2 + y_2 - 2y_2 y + y_2^2 & = & r_2^2\\
x^2 - 2x_3 x + x_3^2 + y^2 - 2y_3 y + y_3^2 & = & r_3^2
\end{array}
$$

#### Stap 3

Door nu de tweede vergelijking van de eerste af te trekken bekomt men:

$$
(-2x_1+2x_2) x + (-2y_1 + 2y_2 ) y = r_1^2 - r_2^2 - x_1^2 + x_2^2 - y_1^2 + y_2^2 
$$

Analoog trekt men de derde vergelijking van de tweede vergelijking af:

$$
(-2x_2+2x_3) x + (-2y_2 + 2y_3 ) y = r_2^2 - r_3^2 - x_2^2 + x_3^2 - y_2^2 + y_3^2 
$$

#### Stap 4

Merk op dat bijna alle waarden hier gegeven zijn. Je kan bovenstaande vergelijkingen herschrijven als:

$$
\begin{array}{rcl}
A x + B y & = & C\\
D x + E y & = & F
\end{array}
$$

De oplossing $$(x_\text{M}, y_\text{M})$$ van dit stelsel wordt nu gegeven door:

$$
\begin{array}{rcl}
x & = & \dfrac{CE - FB}{EA - BD}\\
y & = & \dfrac{CD - AF}{BD - AE}
\end{array}
$$

## Opgave

Schrijf een Python functie `trilateratie( co1, co2, co3, r1, r2, r3 )` dat gegeven drie coördinaten (tupels) van zendmasten `co1`, `co2` en `co3` en drie corresponderende stralen `r1`, `r2` en `r3` het snijpunt van de drie cirkels berekent en op het scherm afdrukt. Rond de coördinaten af op **één cijfer na de komma**.

#### Voorbeeld
```
>>> trilateratie( (0,0), (-2,4), (3,4), 3.00, 2.14, 3.26) 
Locatie mobiele telefoon:
(-0.1, 3.0)
```