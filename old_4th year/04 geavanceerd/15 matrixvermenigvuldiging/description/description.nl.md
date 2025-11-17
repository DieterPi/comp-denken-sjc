## Opgave
Schrijf een functie `matrixvermenigvuldiging()` die gegeven twee matrices het product uitrekent.

Het product van twee matrices $$A$$ en $$B$$ met respectievelijke dimensies $$m \times n$$ en $$n \times k$$ is een matrix $$C$$ met dimensie $$m \times k$$ waarbij voor elk element $$c_{ij}$$ uit matrix $$C$$ geldt:

$$
c_{ij} = \sum_{t=1}^k a_{it} \cdot b_{tj}
$$

Bijvoorbeeld:

$$
\pmatrix{1 & 3\\ 4 & 5} \cdot \pmatrix{0 & 1 \\ -1 & 3} = \pmatrix{-3 & 10 \\ -5 & 19}
$$

TODO: duidelijker uitschrijven
Extra voorbeelden voorzien.

#### Voorbeelden
```
>>> matrixvermenigvuldiging( [[1,3],[4,5]], [[0,1],[-1,3]] )
[[-3, 10], [-5, 19]]
```