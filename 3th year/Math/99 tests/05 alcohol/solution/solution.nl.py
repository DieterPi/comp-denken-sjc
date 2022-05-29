#!/usr/bin/python
# -*- coding: utf-8 -*-

promille = float( input( 'Geef het alcoholpercentage in: ' ) )

print('\n')
if promille >= 0.8:
    print( 'P: U krijgt een rijverbod van 6 uur en moet een ademanalyse doen.' )
elif promille >= 0.5:
    print( 'A: U krijgt een rijverbod van 3 uur en moet een ademanalyse doen.' )
else:
    print( 'S: U mag verder rijden.' )