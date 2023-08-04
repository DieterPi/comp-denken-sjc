#!/usr/bin/python
# -*- coding: utf-8 -*-

def convolutie( source:list, kernel:list ) -> list:
    result = []
    source_len = len( source )
    kernel_len = len( kernel )
    for i in range( source_len + kernel_len // 2 + 1 ):
        sum = 0
        for j in range( kernel_len ):
            index = i - kernel_len + j + 1
            if 0 <= index < source_len:
                sum += kernel[ j ] * source[ index ]
        result.append( round( sum, 1) )
    
    return result
