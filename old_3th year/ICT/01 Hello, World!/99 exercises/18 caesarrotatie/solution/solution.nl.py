#!/usr/bin/python
# -*- coding: utf-8 -*-

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

letter = input( 'Geef een hoofdletter in: ' )
pos = alfabet.find(letter)

print( '{}'.format( alfabet[ ( pos + 13 ) % 26 ] ) )