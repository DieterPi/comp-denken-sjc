Je schreef reeds een programma dat **3 faculteit** berekende, namelijk:

$$
\mathsf{3! = 3 \cdot 2 \cdot 1 = 6}
$$

Per definitie geldt, indien $$\mathsf{n}$$ natuurlijk is:

$$
\mathsf{n! = n \cdot (n-1)\cdot (n-2)\cdot \ldots \cdot 2 \cdot 1 \qquad \text{waarbij } 0! = 1}
$$

## Gevraagd

Schrijf een **recursieve** functie `faculteit(n)` die de faculteit van het getal n teruggeeft.

#### Voorbeelden

```python
>>> faculteit(3)
6
```

```python
>>> faculteit(5)
120
```

{: .callout.callout-info}
> #### Tip
> Je hoeft in dit programma **geen** invoer aan de gebruiker te vragen. Programmeer **enkel** de functie `faculteit(n)`.
