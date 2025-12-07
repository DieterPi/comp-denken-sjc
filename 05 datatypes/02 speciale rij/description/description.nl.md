## Gegeven

Misschien ken je dit raadsel. Geef het volgende getal in deze rij:

$$
\mathsf{1, \qquad 11, \qquad 21, \qquad 1211, \qquad 111221, \qquad \ldots}
$$

Het antwoord is eigenlijk vrij eenvoudig, namelijk: 312211. De rij werd namelijk *taalkundig* opgebouwd. In het getal wordt telkens weergegeven uit hoeveel cijfers het voorgaande getal bestaat.

Na 21 komt 1211, namelijk **één** 2 en **één** 1, genoteerd als 1211.

Na 1211 komt 111221, namelijk **één** 1, **één** 2 en **twee** 1'en.

Na 111221 komt 312211, namelijk **drie** 1'en, **twee*** 2'en en **één** 1.

## Opgave

Schrijf een functie `volgende_getal(getal)` die gegeven één van deze getallen (`getal`) het volgende getal bepaalt.

Gebruik deze functie erna om een nieuwe functie `speciale_rij(n)` te programmeren, met een rangnummer `n` als argument, dat het `n`de getal uit deze speciale rij bepaalt.

#### Voorbeelden

```python
>>> volgende_getal(21)
1211
```

```python
>>> volgende_getal(111221)
312211
```

```python
>>> speciale_rij(3)
21
```

```python
>>> speciale_rij(5)
111221
```

