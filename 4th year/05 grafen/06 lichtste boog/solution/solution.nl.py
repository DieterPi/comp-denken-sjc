#!/usr/bin/python
# -*- coding: utf-8 -*-

def lichtste_boog( E: list ) -> tuple:
    min_e = E[0]
    
    for e in E:
        if e[2] < min_e[2]:
            min_e = e
    
    return min_e
