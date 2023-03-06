#!/usr/bin/python
# -*- coding: utf-8 -*-

def symmetrisch_verschil( inA, inB, inC ):
    if inA and inB and inC:
        output = True
    elif inA and not inB and not inC:
        output = True
    elif inB and not inA and not inC:
        output = True
    elif inC and not inA and not inB:
        output = True
    else:
        output = False

    print(output)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()