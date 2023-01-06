#!/usr/bin/python
# -*- coding: utf-8 -*-

def belasting( inkomen ):
    if inkomen > 41360:
        belasting = (inkomen - 41360) * 0.5 + ( 41360 - 23900 ) * 0.45 + ( 23900 - 13540 ) * 0.4 + 13540 * 0.25
    elif inkomen > 23900:
        belasting = ( inkomen - 23900 ) * 0.45 + ( 23900 - 13540 ) * 0.4 + 13540 * 0.25
    elif inkomen > 13540:
         belasting = ( inkomen - 13540 ) * 0.4 + 13540 * 0.25
    else:
        belasting =  inkomen * 0.25
    
    print( belasting )

if __name__ == '__main__':
    import doctest
    doctest.testmod()