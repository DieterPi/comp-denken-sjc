#!/usr/bin/python
# -*- coding: utf-8 -*-

# Vraagt de gebruiker naar invoer.
gewicht_aarde = float( input( 'Geef je gewicht op aarde in:' ) )

# Voert de berekeningen uit.
gewicht_maan = round( gewicht_aarde / 9.81 * 1.622, 2 )
gewicht_venus = round( gewicht_aarde / 9.81 * 8.87, 2 )
gewicht_mars = round( gewicht_aarde / 9.81 * 3.711, 2 )

# Verzorgt de afdruk op het scherm.
print('')
print( 'Je gewicht op de maan is', gewicht_maan, 'N.' )
print( 'Je gewicht op Venus is', gewicht_venus, 'N.' )
print( 'Je gewicht op Mars is', gewicht_mars, 'N.' )