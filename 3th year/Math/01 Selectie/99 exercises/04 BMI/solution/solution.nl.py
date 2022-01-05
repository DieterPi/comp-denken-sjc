#!/usr/bin/python
# -*- coding: utf-8 -*-

def bmi( massa, lengte ):
    bmi = massa / pow( lengte / 100, 2 )
    if bmi < 18:
        print( 'Een persoon van', massa, 'kg met een lengte van', lengte, 'cm heeft ondergewicht.' )
    elif bmi < 25:
        print( 'Een persoon van', massa, 'kg met een lengte van', lengte, 'cm heeft een normaal gewicht.' )
    elif bmi < 30:
        print( 'Een persoon van', massa, 'kg met een lengte van', lengte, 'cm heeft overgewicht.' )
    else:
        print( 'Een persoon van', massa, 'kg met een lengte van', lengte, 'cm heeft obesitas.' )

if __name__ == '__main__':
    import doctest
    doctest.testmod()