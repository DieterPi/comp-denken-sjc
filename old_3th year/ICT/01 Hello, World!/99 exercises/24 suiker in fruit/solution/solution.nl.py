#!/usr/bin/python
# -*- coding: utf-8 -*-

# Vraagt de gebruiker naar invoer.
hoeveelheid = int( input( 'Geef het aantal gram fruit je zal eten:' ) )

# Voert de berekeningen uit.
suikers_watermeloen = round( hoeveelheid * 6 / 100, 2 )
suikers_banaan = round( hoeveelheid * 12 / 100, 2 )
suikers_appel = round( hoeveelheid * 10 / 100, 2 )
suikers_kiwi = round( hoeveelheid * 9 / 100, 2 )
suikers_druif = round( hoeveelheid * 16 / 100, 2 )

# Verzorgt de afdruk op het scherm.
print()
print( hoeveelheid, 'g watermeloen bevat', suikers_watermeloen, 'g suiker.')
print( hoeveelheid, 'g banaan bevat', suikers_banaan, 'g suiker.')
print( hoeveelheid, 'g appel bevat', suikers_appel, 'g suiker.')
print( hoeveelheid, 'g kiwi bevat', suikers_kiwi, 'g suiker.')
print( hoeveelheid, 'g druiven bevat', suikers_druif, 'g suiker.')