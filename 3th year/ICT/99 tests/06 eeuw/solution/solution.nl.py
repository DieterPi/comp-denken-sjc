#!/usr/bin/python
# -*- coding: utf-8 -*-

jaartal = int( input( 'Geef het jaartal in:' ) )

eeuw = jaartal // 100 + 1

print( '\n{} e eeuw'.format( eeuw ) )