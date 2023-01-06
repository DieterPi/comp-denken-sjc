#!/usr/bin/python
# -*- coding: utf-8 -*-

# Vraagt de gebruiker naar invoer.
n = int( input( 'Geef het rangnummer in:' ) )

# Voert de berekeningen uit.
V_n =  int( n * (3 * n - 1 ) / 2 )

# Verzorgt de afdruk op het scherm.
print('')
print( 'Het', n, 'e vijfhoeksgetal is', V_n )