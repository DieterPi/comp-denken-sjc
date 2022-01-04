#!/usr/bin/python
# -*- coding: utf-8 -*-

getal = int( input( 'Geef een getal van 2 cijfers in: ' ) )

t = getal // 10
e = getal % 10

spiegelbeeld = e * 10 + t

print('\nHet spiegelbeeld van {} is {}'.format( getal, spiegelbeeld ) )