#!/usr/bin/python
# -*- coding: utf-8 -*-

def piraten_puzzel( aantal_piraten: int = 5  ) -> None :
    flag = True
    startaantal = aantal_piraten + 1 # klein aantal kokosnoten als startgok
    j = 0
    while flag:
        aantal = startaantal + j

        # Simuleert het verdeelgedrag, +1 omdat op het einde iedereen wakker is en hetzelfde nog eens gebeurt
        for _ in range( aantal_piraten + 1 ):
            rest = aantal % aantal_piraten
            aantal = aantal // aantal_piraten * ( aantal_piraten - 1 )
            flag = flag and rest == 1
        
        # Loop checks
        if not flag:
            j += 1
            flag = True
        else:
            flag = False

    print( 'Bij', aantal_piraten, 'piraten zijn er', startaantal + j, 'kokosnoten nodig.' )
