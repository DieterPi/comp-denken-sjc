#!/usr/bin/python
# -*- coding: utf-8 -*-
max = int( input( 'Geef het maximum op: ' ) )
lijst = list( range( 1, max + 1 ) )

lijst[0] = 0
for i in lijst:
  if i != 0:
    for k in range( 2, max // i + 1 ):
      lijst[i * k - 1] = 0

priemgetallen = []
for getal in lijst:
  if getal != 0:
    priemgetallen.append( getal )

print('\n{}'.format(priemgetallen) )