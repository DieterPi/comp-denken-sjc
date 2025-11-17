#!/usr/bin/python
# -*- coding: utf-8 -*-

aantalStappen = int( input( 'Hoeveel stappen heb je vandaag reeds gezet? ' ) )

teDoen = 10000 - aantalStappen

print('\nJe dient nog {} stappen te zetten.'.format( teDoen ) )