#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
random.seed(123)

def hoger_lager():
    getal = random.randint( 1, 1000 )

    flag = True
    aantal = 0
    while flag:
        gok = int( input( 'Gok een getal: ' ) )
        aantal += 1
        if gok < getal:
            print( 'Hoger' )
        else:
            print( 'Lager' )
        flag = gok != getal
        
    print( 'Aantal pogingen: ', aantal )
    
hoger_lager()