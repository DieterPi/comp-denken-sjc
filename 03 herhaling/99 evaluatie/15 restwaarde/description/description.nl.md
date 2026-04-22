Bedrijven in Australië kunnen de verminderde waarde van hun apparatuur aangeven in de belastingsaangifte. Als toestellen ouder worden, dan zijn ze immers minder waard, en deze 'minwaarde' kan men ingeven als kosten.

Deze minwaarde kan men berekenen via onderstaande formule:

$$
\mathsf{\text{minwaarde } = \text{waarde vorig jaar } \cdot \dfrac{2}{\text{nuttige levensduur toestel}}}
$$

Als er bijvoorbeeld een server van € 5 000 werd aangekocht met voorziene levensduur van 5 jaar, dan berekent men de minwaarde na één jaar via: $$\textsf{5000 \cdot \dfrac{2}{5}} = 2000$$. Het toestel is na één jaar dus nog € 3 000 waard.

![Foto door Claudio Schwarz op Unsplash.](media/claudio-schwarz.jpg "Foto door Claudio Schwarz op Unsplash."){:data-caption="Foto door Claudio Schwarz op Unsplash." width="40%"}

## Opgave

Schrijf een programma dat de originele aankoopprijs en de voorziene levensduur aan de gebruiker vraagt. Vervolgens bereken je na hoeveel jaar het toestel quasi waardeloos wordt, namelijk indien de waarde minder dan € 1 wordt.

Geef na elk jaar weer hoeveel minwaarde aangegeven kan worden in de belastingsaangift. **Rond** bij alles **af** op twee decimalen.

#### Voorbeelden

Voor een toestel van € `5000.0` met een levensduur van `5` jaar verschijnt:

```
Na het 1 e jaar is de minwaarde: € 2000.0
Na het 2 e jaar is de minwaarde: € 1200.0
Na het 3 e jaar is de minwaarde: € 720.0
Na het 4 e jaar is de minwaarde: € 432.0
Na het 5 e jaar is de minwaarde: € 259.2
Na het 6 e jaar is de minwaarde: € 155.52
Na het 7 e jaar is de minwaarde: € 93.31
Na het 8 e jaar is de minwaarde: € 55.99
Na het 9 e jaar is de minwaarde: € 33.59
Na het 10 e jaar is de minwaarde: € 20.16
Na het 11 e jaar is de minwaarde: € 12.09
Na het 12 e jaar is de minwaarde: € 7.26
Na het 13 e jaar is de minwaarde: € 4.35
Na het 14 e jaar is de minwaarde: € 2.61
Na het 15 e jaar is de minwaarde: € 1.57
Na het 16 e jaar is de minwaarde: € 0.94
Na het 17 e jaar is de minwaarde: € 0.56
Na 17 jaren is het product quasi waardeloos geworden.
```

