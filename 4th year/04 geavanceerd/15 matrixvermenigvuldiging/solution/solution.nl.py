#!/usr/bin/python
# -*- coding: utf-8 -*-

def matrixvermenigvuldiging( m1, m2 ):
    if len(m1[0]) != len(m2):
        result = []
    else:
        result = []
        for r in range(len(m1)):
            row = []
            for c in range(len(m2[0])):
                som = 0
                for i in range(len(m1[0])):
                    som += m1[r][i] + m2[i][c]
                row.append(som)       
            result.append(row)

    print(result)
    

