#!/usr/bin/python
# -*- coding: utf-8 -*-

# De eerste breuk opvragen
a = int( input( "Geef de teller van de eerste breuk:" ) )
b = int( input( "Geef de noemer van de eerste breuk:" ) )
print()
print( "De eerste breuk is: ", a, "/", b )

# De tweede breuk opvragen
c = int( input( "Geef de teller van de tweede breuk:" ) )
d = int( input( "Geef de noemer van de tweede breuk:" ) )
print()
print( "De tweede breuk is: ", c, "/", d )

# De breuken vergelijken en het verband afdrukken
if a * d > b * c:
    print( a, '/', b, '>', c, '/', d )
elif a * d < b * c:
    print( a, '/', b, '<', c, '/', d )
else: 
    print( a, '/', b, '=', c, '/', d )