{: .callout.callout-danger}
> De doorsnede van twee verzamelingen $$A$$ en $$B$$ is gedefinieerd als:
>
> $$A \cap B = \{ x: x\in A \text{ en } x \in B \}$$

## Opgave
Vraag aan de gebruiker de grenzen van twee gesloten intervallen en bepaal vervolgens de doorsnede van deze intervallen.

Er moeten dus **vier** getallen gevraagd worden aan de gebruiker.

#### Voorbeelden

Voor de intervallen [`3`, `5`] en [`-1`, `4`] verschijnt:
```
De doorsnede van [ 3 , 5 ] en [ -1 , 4 ] is [ 3 , 4 ]
```

Voor de intervallen [`-8`, `0`] en [`5`, `10`] verschijnt:
```
De doorsnede van [ -8 , 0 ] en [ 5 , 10 ] is ledig
```

Voor de intervallen [`-2`, `6`] en [`6`, `7`] verschijnt:
```
De doorsnede van [ -2 , 6 ] en [ 6 , 7 ] is singleton 6
```

{: .callout.callout-info}
> #### Tip
> Je kan dit efficiënt programmeren met behulp van de functies `min()` en `max()` om enerzijds het minimum en het maximum te bepalen. Je hoeft dit zeker niet te gebruiken, andere manieren zijn ook mogelijk.