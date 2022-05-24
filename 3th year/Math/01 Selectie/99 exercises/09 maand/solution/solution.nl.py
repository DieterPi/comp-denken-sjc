#!/usr/bin/python
# -*- coding: utf-8 -*-

def aantal_dagen( maandnummer ):
    if ( (maandnummer % 2 != 0 and maandnummer <= 7 ) or maandnummer == 8 or maandnummer == 10 or maandnummer == 12):
        print( 'Maand', maandnummer, 'bevat 31 dagen.')
    elif (maandnummer == 2):
        print( 'Maand', maandnummer, 'bevat 28 dagen.')
    else:
        print( 'Maand', maandnummer, 'bevat 30 dagen.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()