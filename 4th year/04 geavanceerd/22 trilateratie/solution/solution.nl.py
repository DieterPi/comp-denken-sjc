#!/usr/bin/python
# -*- coding: utf-8 -*-

def trilateratie( co1:tuple, co2:tuple, co3:tuple, r1:float, r2:float, r3:float ) -> None:
    A = -2 * co1[0] + 2 * co2[0]
    B = -2 * co1[1] + 2 * co2[1]
    C = r1**2 -r2**2 - co1[0]**2 + co2[0]**2 - co1[1]**2 + co2[1]**2
    D = -2 * co2[0] + 2 * co3[0]
    E = -2 * co2[1] + 2 * co3[1]
    F = r2**2 -r3**2 - co2[0]**2 + co3[0]**2 - co2[1]**2 + co3[1]**2
    
    x = round( ( C * E - F * B ) / ( E * A - B * D ), 1 )
    y = round( ( C * D - A * F ) / ( B * D - A * E ), 1 )
    
    print('Locatie mobiele telefoon:')
    print( ( x , y ) )
