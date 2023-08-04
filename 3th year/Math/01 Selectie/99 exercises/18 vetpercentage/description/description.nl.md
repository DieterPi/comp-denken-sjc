Het vetpercentage geeft de hoeveelheid vet die opgeslagen ligt in je lichaam. Een te hoog of te laag vetpercentage is ongezond, een te hoog vetpercentage leidt tot verhoogde kans op hart- en vaatziekten en diabetes. Maar ook een te laag vetpercentage is ongezond.

![Lichaamsvet.](media/towfiqu-barbhuiya.jpg "Afbeelding door Towfiqu barbhuiya op Unsplash."){:data-caption="Lichaamsvet." width="300px"}

Er zijn heel wat verschillende manieren om het vetpercentage te schatten. Onderstaande methode werd in 1969 bepaald door Jack H. Wilmore en Albert R. Behnke, deze methode geeft een vrij betrouwbare schatting van het vetpercentage. Men dit hierbij de buikhuidplooi $$\mathsf{Ab}$$ en de huidplooi van een bovenbeen $$\mathsf{Th}$$ te meten. Deze afmetingen (in mm) vult men in in onderstaande formule:

$$
mathsf{ BD = 1,08543 - (0,000886 \cdot Ab) - (0,0004 \cdot Th) }
$$

Hierbij stelt $$\mathsf{BD}$$ de lichaamsdichtheid uit. Vervolgens kan men het vetpercentage uitrekenen met de formule van Siri (onderzocht door William E. Siri):

$$
mathsf{ \dfrac{4,95}{BD} - 4,50 }
$$

## Opgave
Schrijf een functie `vetpercentage( ab, th )` die gegeven de twee metingen van de huidplooien het vetpercentage afdrukt.

#### Voorbeeld
```
>>> vetpercentage( 15.8, 8.7 )
2.77
```