#!/usr/bin/python
# -*- coding: utf-8 -*-

def schaakbord( r, k ):
    teller = 0
    for _ in range(r):
        rij = ''
        for _ in range(k):
            if teller % 2 == 0:
                rij += ' x '
            else:
                rij += ' . '
            teller += 1
        teller += k % 2 == 0
        print( rij )

if __name__ == '__main__':
    import doctest
    doctest.testmod()
