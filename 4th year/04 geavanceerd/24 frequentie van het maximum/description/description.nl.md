## Opgave
Schrijf een functie `aantal_max()` die gegeven een matrix op het scherm afdrukt wat het grootste element is en op welke plaatsen dit element voorkomt.

{: .callout.callout-info}
> #### Tip
> Schrijf eerst een functie `bepaal_max()` die het grootste element van de matrix bepaalt.

#### Voorbeelden
Indien onderstaande matrix als argument wordt meegegeven verschijnt er:

$$
\begin{pmatrix}
4 & 3 & 1 & 2\\
-1 & 0 & 3 & 4\\
0 & 4 & 2 & 1
\end{pmatrix}
$$

```
>>> aantal_max( [ [4,3,1,2], [-1,0,3,4], [0,4,2,1] ] ) 
Het grootste element uit de matrix is 4 en dit staat op de plaatsen:
rij: 1 , kolom: 1
rij: 2 , kolom: 4
rij: 3 , kolom: 2
```