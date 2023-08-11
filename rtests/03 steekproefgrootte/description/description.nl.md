Om een steekproefgrootte $$n$$ te bepalen gebruikt me vaak onderstaande vuistregel.

$$
    n = \dfrac{\lambda^2\cdot p \cdot (1-p)}{d^2}
$$

Hierbij stelt $$\lambda$$ een waarde voor gebaseerd op de nauwkeurigheid die men wilt, zie onderstaande tabel, $$p$$ de steekproefverhouding (meestal gebruikt men 0,5) en $$d$$ de foutenmarge.

| betrouwbaarheid |  λ |
|:--------:|-------------|
| 90 % | 1,65 |
| 95 % | 1,96 |
| 99 % | 2,58 |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

## Opgave
Pas het onderstaande programma aan zodat de benodigde steekproefgrootte berekend wordt.