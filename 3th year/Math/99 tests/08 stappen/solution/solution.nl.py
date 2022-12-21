#!/usr/bin/python
# -*- coding: utf-8 -*-

aantalStappen = int( input( 'Hoeveel stappen heb je vandaag reeds gezet? ' ) )

teDoen = 10000 - aantalStappen

if( aantalStappen < 10000 ):
    print('\nJe dient nog {} stappen te zetten.'.format( teDoen ) )
else: 
    print('\nJe hebt je stappendoel van vandaag reeds bereikt.')