#!/usr/bin/python
# -*- coding: utf-8 -*-

temperatuur = float( input( 'Geef de huidige temperatuur in: ') )

# berekening
afwijking = abs( temperatuur - 10 )

# weergeven op het scherm
print( 'Afwijking:', round( afwijking, 1 ) )