#!/usr/bin/python
# -*- coding: utf-8 -*-

def matrixvermenigvuldiging( m1:list, m2:list ) -> list:
    if len( m1[0] ) != len( m2 ):
        result = []
    else:
        result = []
        for m1row in m1:
            row = []
            for c in range( len( m2[0] ) ):
                som = 0
                for i in range( len( m1[0] ) ):
                    som += m1row[i] * m2[i][c]
                row.append( som )
            result.append( row )

    return result

