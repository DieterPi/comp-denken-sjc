#!/usr/bin/python
# -*- coding: utf-8 -*-

def lichtste_boog( E: list ) -> None:
    min_e = E[0]
    
    for e in E:
        if e[2] < min_e[2]:
            min_e = e
    
    print( 'De boog die', min_e[0], 'en', min_e[1], 'verbindt met gewicht', min_e[2], 'heeft het kleinste gewicht.')
