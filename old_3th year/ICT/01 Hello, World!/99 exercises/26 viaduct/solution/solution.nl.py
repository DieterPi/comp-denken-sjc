#!/usr/bin/python
# -*- coding: utf-8 -*-

# Vraagt de gebruiker naar invoer.
l = int( input( 'Geef de lengte in in:' ) )
n = int( input( 'Geef het aantal bogen in:' ) )

# Voert de berekeningen uit.
b = round( l / n, 2 )

# Verzorgt de afdruk op het scherm.
print('')
print( 'breedte:', b, 'm' )