#!/usr/bin/python
# -*- coding: utf-8 -*-

getal1 = int(input('Geef een eerste getal in: ' ))
getal2 = int(input('Geef een tweede getal in: '))

A = max(getal1, getal2)
B = min(getal1, getal2)

rest = A % B
while rest != 0:
  A = B
  B = rest
  rest = A % B

print('\nDe grootste gemene deler van {} en {} is {}'.format( getal1, getal2, B ) )