#!/usr/bin/python
# -*- coding: utf-8 -*-

def energieklasse( lichtstroom, energieverbruik ):
    efficientie = lichtstroom / energieverbruik
    
    if( efficientie >= 210 ):
        label = 'A'
    elif( efficientie >= 185):
        label = 'B'
    elif( efficientie >= 160):
        label = 'C'
    elif( efficientie >= 135):
        label = 'D'
    elif( efficientie >= 110):
        label = 'E'
    elif( efficientie >= 85):
        label = 'F'
    else:
        label = 'G'
    
    print('Energieklasse:', label)

if __name__ == '__main__':
    import doctest
    doctest.testmod()