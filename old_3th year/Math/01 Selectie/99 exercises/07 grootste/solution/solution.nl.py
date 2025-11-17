#!/usr/bin/python
# -*- coding: utf-8 -*-

getal1 = float( input( 'Geef een eerste getal in: ' ) )
grootste = getal1

getal2 = float( input( 'Geef een tweede getal in: ' ) )
if getal2 > grootste :
    grootste = getal2
    
getal3 = float( input( 'Geef een derde getal in: ' ) )
if getal3 > grootste :
    grootste = getal3
    
print('\nHet grootste getal was', grootste)
