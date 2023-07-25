#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

def hoger_lager():
    getal = random.randint( 1, 1000 )

    flag = True
    aantal = 0
    while flag:
        gok = int( input( 'Gok een getal: ' ) )
        aantal += 1
        if gok < getal:
            print( 'Hoger' )
        elif gok > getal:
            print( 'Lager' )
        flag = gok != getal
        
    return 'Aantal pogingen: {}'.format( aantal ) 
    
hoger_lager()