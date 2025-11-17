#!/usr/bin/python
# -*- coding: utf-8 -*-

def bakshali_methode( grondtal, startwaarde ):
    getal1 = startwaarde
    verschil = 1
    i = 0
    while verschil > pow( 10, -12):
        a = (grondtal - getal1**2)/(2*getal1)
        b = getal1 + a
        getal2 = b-a**2/(2*b)
        print(i,':',  getal1 )
        verschil = abs(getal2 - getal1)
        getal1 = getal2
        i += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()