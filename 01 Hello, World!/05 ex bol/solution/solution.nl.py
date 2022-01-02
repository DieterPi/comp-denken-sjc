#!/usr/bin/python
# -*- coding: utf-8 -*-
PI = 3.141592
straal = float(input( 'Geef de straal van de bol in (in cm): ' ))

oppervlakte = 4*PI*pow(straal, 2)
volume = 4/3*PI*pow(straal, 3)

print("\noppervlakte: {} cm²".format(round(oppervlakte,2)))
print("volume: {} cm³".format(round(volume,2)))