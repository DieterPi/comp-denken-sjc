Je kan een fractaal in één dimensie tekenen door steeds eenzelfde proces te herhalen. Hieronder vind je een voorbeeld van een eenvoudige fractaal door de figuur steeds te kopieren en deze in het midden *langer* te maken.

![Een eenvoudige fractaal.](media/image.png "Een eenvoudige fractaal."){:data-caption="Een eenvoudige fractaal." .light-only width="450px"}

![Een eenvoudige fractaal.](media/image_dark.png "Een eenvoudige fractaal."){:data-caption="Een eenvoudige fractaal." .dark-only width="450px"}

## Opgave

Schrijf een **recursieve** functie `lijn(n)` die een fractaal met deze *hoogte* op het scherm tekent. Voor de eenvoud, teken je dit echter onder elkaar.

Gebruik hierbij `print("-" * i)` waarbij `i` het aantal streepjes voorstelt.

#### Voorbeelden

```python
>>> lijn(2)
-
--
-
```

```python
>>> lijn(3)
-
--
-
---
-
--
-
```

```python
>>> lijn(5)
-
--
-
---
-
--
-
----
-
--
-
---
-
--
-
```
