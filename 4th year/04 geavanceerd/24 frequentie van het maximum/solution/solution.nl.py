#!/usr/bin/python
# -*- coding: utf-8 -*-

def bepaal_max( m: list ) -> int:
    maximum = m[0][0]
    for row in m:
        for item in row:
            if item > maximum:
                maximum = item
    return maximum

def aantal_max( m: list ) -> None:
    maximum = bepaal_max( m )
    print( 'Het grootste element uit de matrix is', maximum, 'en dit staat op de plaatsen:' )
    for r in range( len( m ) ):
        for c in range( len( m[0] ) ):
            if m[r][c] == maximum:
                print('rij:', r + 1 , ', kolom:', c + 1 )
