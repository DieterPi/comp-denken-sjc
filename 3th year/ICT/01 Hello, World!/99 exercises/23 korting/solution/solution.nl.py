#!/usr/bin/python
# -*- coding: utf-8 -*-

# Vraagt de gebruiker naar invoer.
kortingsprijs = float( input( 'Geef het kortingsbedrag in:' ) )
kortingspercentage = float( input( 'Geef het kortingspercentage in:' ) )

# Voert de berekeningen uit.
prijs = round( kortingsprijs / ( 100 - kortingspercentage ) * 100, 2)

# Verzorgt de afdruk op het scherm.
print('')
print( 'De oorspronkelijke prijs was €', prijs )