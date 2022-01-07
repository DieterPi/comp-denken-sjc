## Opgave
Schrijf een functie `diagonaal()` die gegeven een parameter `n` (een natuurlijk getal < 10) een vierkant afdrukt waarbij:

    Op de hoofddiagonaal `0` staat.
    Op de twee naburige diagonalen `1` staat.
    Op de daaropvolgende diagonalen `2` staat.
    enz... 

#### Voorbeeld
```
>>> diagonaal( 3 )
 0  1  2 
 1  0  1 
 2  1  0 
>>> diagonaal( 5 ) 
 0  1  2  3  4 
 1  0  1  2  3 
 2  1  0  1  2 
 3  2  1  0  1 
 4  3  2  1  0 
```