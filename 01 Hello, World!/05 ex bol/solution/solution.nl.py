#!/usr/bin/python
# -*- coding: utf-8 -*-
PI = 3.141592
straal = float(input( 'Geef de straal van de bol in (in cm): ' ))

oppervlakte = 4*PI*pow(straal, 2)
volume = 4/3*PI*pow(straal, 3)

print("\noppervlakte: {} cm²\nvolume: {} cm³".format(round(oppervlakte,2),round(volume,2)))