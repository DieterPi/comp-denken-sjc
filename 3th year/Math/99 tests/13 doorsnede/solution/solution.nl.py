#!/usr/bin/python
# -*- coding: utf-8 -*-

def doorsnede( interval1, interval2 ):
    a = interval1[0]
    c = interval1[1]
    
    b = interval2[0]
    d = interval2[1]
    
    e = max(a,b)
    f = min(c,d)
    
    if e < f:
        print( 'De doorsnede van [',a ,',',c,'] en [', b,',',d,'] is [',e, ',',f,']')
    elif e == f:
        print( 'De doorsnede van [',a ,',',c,'] en [', b,',',d,'] is singleton',e)
    else: 
        print( 'De doorsnede van [',a ,',',c,'] en [', b,',',d,'] is ledig')


if __name__ == '__main__':
    import doctest
    doctest.testmod()