#!/usr/bin/python
# -*- coding: utf-8 -*-

aantalStappen = int( input( '' ) )

teDoen = 10000 - aantalStappen

if( aantalStappen < 9999 ):
    print('\nJe dient nog {} stappen te zetten.'.format( teDoen ) )
elif (aantalStappen == 9999):
    print('\nJe moet maar één stap meer zetten.')
else: 
    print('\nJe hebt je stappendoel van vandaag reeds bereikt.')