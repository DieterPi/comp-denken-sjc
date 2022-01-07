Bij een 3D-printer worden de motoren bestuurd door kleine electronica bordjes, *drivers*. De A4988 is een van de meeste gebruikte drivers. Opdat de driver goed werkt moet de electrische spanning $$V_{\text{ref}}$$ correct worden ingesteld. Dit gebeurt met de volgende formule:

$$
V_{\text{\ref}} = 8\cdot 0,05 \cdot I
$$

waarbij $$I$$ de stroomsterkte voorstelt die de motor nodig heeft.

![3d printer](media/3dprinter.jpg "3d printer"){:data-caption="Een 3D-printer" width="35%"}

## Opgave
Schrijf een programma dat voor een gegeven $$V_{\text{ref}}$$ de stroomsterkte uitrekent. Rond af op 3 cijfers na de komma.

#### Voorbeeld
De input `38` geeft als output:
```
Het spiegelbeeld van 38 is 83
```

De input `51` geeft als output:
```
Het spiegelbeeld van 51 is 15
```
