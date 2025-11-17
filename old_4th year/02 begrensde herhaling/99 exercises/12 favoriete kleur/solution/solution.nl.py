#!/usr/bin/python
# -*- coding: utf-8 -*-

lijst = [('Alixe', 'indigo'), ('Anthe', 'groen'), ('Cara', 'geel'), ('Célia', 'oranje'), ('Dionah', 'violet'), ('Divine', 'geel'), ('Dorcas', 'indigo'), ('Eliana', 'geel'), ('Eliane', 'groen'), ('Elien', 'oranje'), ('Eline', 'indigo'), ('Elise', 'violet'), ('Emma', 'oranje'), ('Feliz', 'indigo'), ('Fiebe', 'blauw'), ('Fleur', 'oranje'), ('Fran', 'rood'), ('Geike', 'violet'), ('Grace', 'indigo'), ('Griet', 'geel'), ('Guilia', 'oranje'), ('Hannah', 'violet'), ('Hanne', 'groen'), ('Hayley', 'rood'), ('Heleen', 'oranje'), ('Helena', 'indigo'), ('Inès', 'geel'), ('Iris', 'geel'), ('Isolde', 'violet'), ('Jade', 'indigo'), ('Jinte', 'blauw'), ('Jitske', 'groen'), ('Julia', 'rood'), ('Julie', 'groen'), ('Kawtar', 'violet'), ('Kyra', 'blauw'), ('Lien', 'violet'), ('Lina', 'oranje'), ('Linde', 'oranje'), ('Lisa', 'oranje'), ('Lore', 'rood'), ('Lotte', 'groen'), ('Mareta', 'violet'), ('Marie', 'oranje'), ('Marthe', 'geel'), ('Méira', 'geel'), ('Mira', 'groen'), ('Myrthe', 'indigo'), ('Naya', 'blauw'), ('Nele', 'groen'), ('Nette', 'indigo'), ('Nienke', 'rood'), ('Nina', 'groen'), ('Noor', 'violet'), ('Renée', 'geel'), ('Sara', 'rood'), ('Sofie', 'blauw'), ('Sosena', 'violet'), ('Stella', 'oranje'), ('Stien', 'blauw'), ('Stina', 'groen'), ('Thalia', 'oranje'), ('Tille', 'rood'), ('Tinka', 'indigo'), ('Xanthe', 'blauw'), ('Yana', 'geel'), ('Yente', 'rood'), ('Yorunn', 'violet')]

def favoriete_kleur( kleur ):
    aantal = 0
    for item in lijst:
        aantal += item[1] == kleur
    
    print( aantal ) 

if __name__ == '__main__':
    import doctest
    doctest.testmod()