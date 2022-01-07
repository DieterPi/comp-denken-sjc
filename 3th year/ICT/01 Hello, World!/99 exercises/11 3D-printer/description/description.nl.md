Bij een 3D-printer worden de motoren bestuurd door kleine electronica bordjes genaamd *drivers*. De A4988 is een van de meeste gebruikte drivers. Opdat de driver goed werkt moet de elektrische spanning $$V_{\text{ref}}$$ correct worden ingesteld. Dit gebeurt met de volgende formule:

$$
V_{\text{ref}} = 8\cdot 0,05 \cdot I
$$

waarbij $$I$$ de stroomsterkte voorstelt die de motor nodig heeft.

![3d printer](media/3dprinter.jpg "3d printer"){:data-caption="Een 3D-printer" width="30%"}

## Opgave
Schrijf een programma dat voor een ingelezen $$V_{\text{ref}}$$ de stroomsterkte uitrekent. Rond af op 3 cijfers na de komma.

#### Voorbeeld
De input `0.574` geeft als output:
```
De stroomsterkte is 1.435
```